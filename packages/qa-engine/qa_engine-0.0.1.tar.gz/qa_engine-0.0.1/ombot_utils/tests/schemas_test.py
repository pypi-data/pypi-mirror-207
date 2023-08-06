from ombot_utils import schemas, logging
import os

os.environ.setdefault('IS_DEBUG', 'true')
logging.init_logger('ombot', 'ombot')


records = {
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
records = schemas.ChatRecords(**records)

recent = records.get_recent(num=10)
print(recent)

for message in records:
    print(message.content)