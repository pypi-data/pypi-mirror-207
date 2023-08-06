import os
import yaml
import json


class EnvVars(object):
    APP_VERSION = "1.0"
    root_dir = os.path.dirname(os.path.realpath(__file__))

    default = yaml.load(
        open(os.path.join(root_dir, "config.yaml"), "r"), Loader=yaml.FullLoader
    )
    APP_NAME = "OmBot-QA"
    API_PREFIX = "/ombot"
    IS_DEBUG = bool(os.environ.get("IS_DEBUG", default["IS_DEBUG"]))
    SERVER_NAME = os.environ.get("SERVER_NAME", default["SERVER_NAME"])
