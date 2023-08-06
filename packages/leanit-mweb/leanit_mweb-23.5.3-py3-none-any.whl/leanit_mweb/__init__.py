from __future__ import annotations
import logging
import os
from os.path import isabs, abspath
import yaml

from leanit_mweb.jinja_template import Jinja2Templates
from leanit_mweb.jinja_template.loaders import FileSystemLoader
from leanit_mweb.yuga import YugabytedbThreadPool

logger = logging.getLogger(__name__)

from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    pass

config: Dict = None
db: YugabytedbThreadPool = None
loader: FileSystemLoader = None
templates: Jinja2Templates = None

def _read_config(app_root: str) -> Dict:
    config_data = {}
    config_profile = os.environ.get("CONFIG_PROFILE", "default")
    config_dir = f"{app_root}/etc/{config_profile}"

    for config_file in os.listdir(config_dir):
        # only read .yml and .yaml files
        if not config_file.endswith(".yml") and not config_file.endswith(".yaml"):
            continue
        config_file_abs = f"{config_dir}/{config_file}"

        logger.info(f"Reading config from {config_file_abs}")

        # read yaml config
        with open(config_file_abs, "r") as f:
            config_data.update(yaml.safe_load(f))

    return config_data


def init(app_root: str):
    """
    :param app_root: path to the root of the application
    :return:
    """
    global config
    config = _read_config(app_root)

    global db
    pool_config = config["db"].get("pool", {})
    db = YugabytedbThreadPool(
        min_workers=pool_config.get("min_workers", 1),
        max_workers=pool_config.get("max_workers", 10),
    )
    db.migrate(migration_dir=f"{app_root}/migrations")

    # get all subclasses of Model
    from leanit_mweb.orm.model import Model
    # initialize all models
    for cls in Model.__subclasses__(): # type: Model
        cls._initialize()

    global loader, templates
    loader = FileSystemLoader(f"{app_root}/templates")
    templates = Jinja2Templates(directory=f"{app_root}/templates", loader=loader)
