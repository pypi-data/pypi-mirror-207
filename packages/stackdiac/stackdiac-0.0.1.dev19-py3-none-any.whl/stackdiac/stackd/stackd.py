import copy
import logging, yaml, os
import time
from urllib.parse import urlparse

from pydantic import parse_obj_as, BaseModel
from typing import Any
import subprocess
from deepmerge import always_merger


from stackdiac import models
from stackdiac.models.provider import Provider



logger = logging.getLogger(__name__)

class StackdCounters(BaseModel):
    clusters: int = 0
    stacks: int = 0
    modules: int = 0
    time: float = 0.0

    start_time: float = 0.0

    def reset(self):
        self.clusters = 0
        self.stacks = 0
        self.modules = 0
        self.time = 0
        self.start_time = time.time()

    def stop(self):
        self.time = time.time() - self.start_time

    def __str__(self) -> str:
        return f"<StackdCounters clusters: {self.clusters} stacks: {self.stacks} modules: {self.modules} time: {self.time:.4f}s>"

    def stats_message(self):
        return f"clusters: {self.clusters} stacks: {self.stacks} modules: {self.modules} time: {self.time:.4f}s"
    

class Stackd(BaseModel):
    
    conf: models.Config | None = None
    root: str = os.environ.get("STACKD_ROOT", ".")
    clusters: dict[str, models.Cluster] = {}    
    providers: dict[str, models.Provider] = {}
    counters: StackdCounters = StackdCounters()

    class Config:
        orm_mode = True
        exceptions = True
        exclude = {"versions", "counters"}
   #     exclude = {'clusters', 'versions', 'conf'}

    @property
    def dns_zone(self) -> str:
        return self.conf.project.domain

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.root = os.path.abspath(self.root)
        if not os.path.isfile(self.config_file):
            logger.warning(f"{self} config file {self.config_file} not found. starting unconfigured.")
        else:
            logger.debug("don't forget to run configure()")

    @property
    def builddir(self):
        return os.path.join(self.root, "build")

    def configure(self):
        
        from ..models import config

        os.chdir(self.root)
        logger.debug(f"{self} chdir to {self.root}")

        with open(self.config_file) as f:
            conf_data = models.get_initial_config(name="unconfigured", domain="example.com", vault_address="http://127.0.0.1:9090").dict()
            initial = copy.deepcopy(conf_data)
            data = yaml.safe_load(f.read())
            conf_data = always_merger.merge(conf_data, data)
            self.conf = parse_obj_as(config.Config, conf_data)
            logger.debug(f"{self} loaded config: conf: {self.conf} \n\n data: {data} \n\n initial: {initial}\n\n")

        if os.path.isfile(self.resolve_path("core:versions.yaml")):
            with open(self.resolve_path("core:versions.yaml")) as f:
                versions_data = yaml.safe_load(f.read())
                if self.conf.providers:
                    versions_data = always_merger.merge(versions_data, self.conf.dict()["providers"])
                self.providers = parse_obj_as(dict[str, models.Provider], versions_data)
                for name, v in self.providers.items():
                    v.name = name
                    
                logger.debug(f"{self} loaded providers: {self.providers}")

        if os.path.isdir(self.conf.clusters_dir):
            for c in os.listdir(self.conf.clusters_dir):
                with open(os.path.join(self.conf.clusters_dir, c)) as f:
                    cname = c.split(".")[0]
                    if cname == "globals": continue
                    data = yaml.safe_load(f.read())[cname]
                    
                    if data.get("kind", None) == "cluster":
                        self.clusters[cname] = parse_obj_as(models.Cluster, data)                        
                    
        self.counters.reset()
        logger.debug(f"{self} loaded clusters: {tuple(self.clusters.keys())}")
        logger.info(f"{self} configured with {len(self.conf.repos)} repos {len(self.clusters)} clusters: {list(self.clusters.keys())}")


    def initialize(self):      
               
        for r in self.conf.repos.values():
            r.stackd = self

        # for b in dict(self.conf.binaries).values():
        #     b.stackd = self
        
        logger.debug("%s initializing at %s", self, os.getcwd())

        os.makedirs(self.dataroot, exist_ok=True)
        os.makedirs(self.cacheroot, exist_ok=True)

    @property
    def dataroot(self):
        return os.path.join(self.root, ".stackd")
        
    @property
    def cacheroot(self):
        return os.path.join(self.dataroot, "cache")    

    def __str__(self):
        try:
            return f"<{self.__class__.__name__} {self.conf.project.name}>"
        except AttributeError as e:
            return f"<{self.__class__.__name__} unconfigured>"

    @property
    def config_file(self):
        return os.path.join(self.root, "stackd.yaml")

    def update(self):
        logger.debug("%s performing update", self)
        for _, r in self.conf.repos.items():
            r.checkout()
            #r.install()
            logger.info(f"{r} repo synced")

    def download_binaries(self):
        assert self.conf is not None
        for b in dict(self.conf.binaries).values():
            b.download()

    def build(self, **kwargs):
        self.counters.reset()
        #logger.debug("%s performing build %s", self, kwargs)
        cluster = kwargs.pop("cluster", "all")
        if cluster == "all":
            for _, c in self.clusters.items():
                c.build(sd=self, **kwargs)
        else:
            self.clusters[cluster].build(sd=self, **kwargs)
        
        self.counters.stop()
    
        logger.info(f"{self} build {self.counters.clusters} clusters, {self.counters.stacks} stacks, {self.counters.modules} modules in {self.counters.time:.4f} seconds")

    def resolve_stack_path(self, src):
        """
        Resolve a stack path to a local path
        repo can be specified as scheme: prefix
        if not specified, stack.yaml is assumed
        """
        parsed_src = urlparse(src)
        if not parsed_src.scheme:
            parsed_src = urlparse(f"root:{src}") # add root repo
        if len(self.src.split("/")) == 1:
            parsed_src = urlparse(f"{parsed_src.scheme}:stack/{src}") # add stack dir

        repo = self.conf.repos[parsed_src.scheme]

        if self.src.endswith(".yaml"):
            path = os.path.join(repo.repo_dir, parsed_src.path.lstrip("/"))           
        else:
            path = os.path.join(repo.repo_dir, parsed_src.path.lstrip("/"), "stack.yaml")
        
        return path


    def resolve_path(self, src):
        """
        Resolve a module path to a local path
        repo can be specified as scheme: prefix
        """
        parsed_src = urlparse(src)
        if not parsed_src.scheme:
            parsed_src = urlparse(f"root:{src}") # add root repo
       
        repo = self.conf.repos[parsed_src.scheme]
        return os.path.join(repo.repo_dir, parsed_src.path)
    
    resolve_module_path = resolve_path

    def terragrunt(self, target, terragrunt_options:list[str], **kwargs):
        env = dict(
            TERRAGRUNT_WORKING_DIR=target,
            TERRAGRUNT_TFPATH=self.conf.binaries.terraform.abspath,
            TF_INPUT="false",
        )
        opts = " ".join(terragrunt_options)
        cmd = f"{self.conf.binaries.terragrunt.abspath} {opts}"
        logger.debug(f"{self} terragrunt {target} {cmd} {env}")

        process = subprocess.Popen(cmd, shell=True, env=dict(**os.environ, **env))
        process.wait()

    def run_operation(self, target, **kwargs):
        """
        target is in form <cluster>/<stack>/<operation>
        running  self.terragrunt with configured module path
    
        """
        cluster, stack, operation = target.split("/")
        self.clusters[cluster].stacks[stack].build(cluster=self.clusters[cluster], sd=self, **kwargs)
        self.clusters[cluster].stacks[stack].stack.operations[operation].run(target=target, sd=self, 
            cluster=self.clusters[cluster],
            stack=self.clusters[cluster].stacks[stack],**kwargs)
        