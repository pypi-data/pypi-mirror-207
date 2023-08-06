# QA engine

OMBot项目的QA引擎，提供项目问答功能
## 使用方法
### 1. 触发闲聊模式
```python
from qa_engine import QAEngine
from ombot_utils.schemas import ChatRecords

if __name__ == '__main__':
    qa = QAEngine()

    records = {
        "bot_id": "2",
        "session_id": "string",
        "callback": "string",
        "messages": [
            {
                "role": "user",
                "message_type": "image",
                "src_type": "url",
                "content": "https://minio/hzlh/omintel/cess/c25f30559b974c728e5dbe1d4177aa5a.jpg",
                "objects": []
            },
            {
                "role": "user",
                "message_type": "text",
                "src_type": "text",
                "content": "你好，请问你是谁？",
                "objects": []
            }
        ]
    }
    records = ChatRecords(**records)
    qa.run(bot_id="2", chat_records=records)
```
### 1. 触发专业模式
```python
from qa_engine import QAEngine
from ombot_utils.schemas import ChatRecords

if __name__ == '__main__':
    qa = QAEngine()

    records = {
        "bot_id": "2",
        "session_id": "string",
        "callback": "string",
        "messages": [
            {
                "role": "user",
                "message_type": "image",
                "src_type": "url",
                "content": "https://minio/hzlh/omintel/cess/c25f30559b974c728e5dbe1d4177aa5a.jpg",
                "objects": []
            },
            {
                "role": "user",
                "message_type": "text",
                "src_type": "text",
                "content": "视频中有人摔倒吗？",
                "objects": []
            }
        ]
    }
    records = ChatRecords(**records)
    qa.run(bot_id="2", chat_records=records)
```