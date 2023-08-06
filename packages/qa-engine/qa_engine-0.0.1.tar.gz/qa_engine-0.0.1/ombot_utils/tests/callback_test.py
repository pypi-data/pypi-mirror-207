from ombot_utils import Callback, schemas, logging
import os

os.environ.setdefault('IS_DEBUG', 'true')
logging.init_logger('ombot', 'ombot')


callback = Callback(bot_id='bot', session_id='1', endpoint='http://')


message = {
    "role": "assistant",
    "message_type": "image",
    "src_type": "url",
    "content": "https://minio/hzlh/omintel/cess/c25f30559b974c728e5dbe1d4177aa5a.jpg",
    "objects": [
        {
            "bbox": [57.0, 982.0, 322.0, 1170.0],
            "label": "食物",
            "conf": 0.5658881068229675,
            "attr": [],
        },
        {
            "bbox": [65.0, 655.0, 262.0, 832.0],
            "label": "食物",
            "conf": 0.5577515363693237,
            "attr": [],
        },
    ],
}
message = schemas.Message(**message)
callback.call(message, schemas.OPT.CHAT_STATUS.END_ANSWER)

callback.error('Test error')
