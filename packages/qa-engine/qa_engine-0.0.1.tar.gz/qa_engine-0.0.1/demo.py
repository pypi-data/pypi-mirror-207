from qa_engine import QAEngine
from ombot_utils.schemas import ChatRecords

if __name__ == '__main__':
    qa = QAEngine()

    records = {
        "bot_id": "1013",
        "session_id": "string",
        "callback": "string",
        "messages": [
            {
                "role": "user",
                "message_type": "text",
                "src_type": "text",
                # "content": "视频中出现过几次饮料打翻吗？发生在什么时候？",
                "content": "打翻的饮料出现在什么时候",
                "objects": []
            }
        ]
    }
    records = ChatRecords(**records)
    qa.process(bot_id="1013", chat_records=records, events=["打翻的饮料"])