from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class KwargsBody(BaseModel):
    events: list[str]

class ChatBody(BaseModel):
    bot_id: str = Field(title='机器人id')
    src_type: str = Field(title='数据类型')
    data: str = Field(title='问题')
    kwargs: KwargsBody



