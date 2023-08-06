from ombot_utils import logging, schemas
from ombot_utils.base import BaseQAEngine
import os

# 设置调试模式
os.environ.setdefault('IS_DEBUG', 'true')

# 初始化logger
logging.init_logger('ombot', 'ombot')


class TestQAEngine(BaseQAEngine):
    def _call(self, bot_id, chat_records):
        logging.info('Do something')


test_input = {
    "bot_id": "string",
    "session_id": "string",
    "callback": "string",
    "messages": [
        {
            "role": "user",
            "message_type": "image",
            "src_type": "url",
            "content": "https://minio/hzlh/omintel/cess/c25f30559b974c728e5dbe1d4177aa5a.jpg",
            "objects": [],
        },
        {
            "role": "user",
            "message_type": "text",
            "src_type": "text",
            "content": "请找出图片中的食物",
            "objects": [],
        },
    ],
}

test_input = schemas.ChatRecords(**test_input)
TestQAEngine().run(test_input.bot_id, test_input)
