import os
import json


class EnvVars(object):
    R2BASE_URL = os.environ.get("R2BASE_URL", "http://192.1.2.230:8000")
    SBERT_URL = os.environ.get("SBERT_URL", "http://192.1.2.239:30031/v1/query/plugin")
    CHATGPT_URL = os.environ.get(
        "CHATGPT_URL", "http://76.147.0.140:8080/chatgpt/v1/serving/chatcompletion"
    )
    CHATGLM_URL = os.environ.get(
        "CHATGLM_URL", "http://10.8.23.24:9018/"
    )
    # INDEX_ID = os.environ.get("INDEX_ID", "guodian_qa")
    INDEX_ID = os.environ.get("INDEX_ID", "security_white_paper")

    @classmethod
    def deepcopy(cls, x):
        return json.loads(json.dumps(x))
