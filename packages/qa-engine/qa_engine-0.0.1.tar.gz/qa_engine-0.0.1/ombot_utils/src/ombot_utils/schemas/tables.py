from typing import Any, Optional, List
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Text
from ..schemas import DetObject


class EventObject(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        '''

        '''
        super().__init__(**data)

    event_name: str
    weight: float
    detailed_events: List[str]
    status: str
    action: str
    solver_event: str


class MemoryObject(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        '''

        '''
        super().__init__(**data)
        image_time: str
        label: str
        score: float


class OmbotEvent(SQLModel, table=True):
    __tablename__ = 'ombotevent'
    id: Optional[int] = Field(default=None, primary_key=True)
    bot_id: str = Field(index=True)
    create_time: str = ''
    update_time: Optional[str] = ''
    event_name: str
    event: str
    source: str = Field(default="decision", include=["init", "decision"])
    character_id: int = 0
    deleted: int = 0


class OmbotCharacter(SQLModel, table=True):
    __tablename__ = 'ombotcharacter'
    id: Optional[int] = Field(default=None, primary_key=True)
    bot_id: str = Field(index=True)
    create_time: str = ''
    update_time: Optional[str] = ''
    character: str #= Field(Column(String(150)))
    traits: str #= Field(Column(String(500)))
    status: str #= Field(Column(String(500)))
    deleted: int = 0


class OmbotMemory(SQLModel, table=True):
    __tablename__ = 'ombotmemory'
    id: Optional[int] = Field(default=None, primary_key=True)
    bot_id: str = Field(index=True)
    create_time: str = ''
    update_time: Optional[str] = ''
    memory: str = Field(sa_column=Column(Text(),nullable=False))
    od_result: str = Field(sa_column=Column(Text(),nullable=True))
    od_result_summary: str = Field(sa_column=Column(Text(),nullable=False))
    caption: str = Field(sa_column=Column(Text(),nullable=False))
    caption_summary: str = Field(sa_column=Column(Text(),nullable=False))
    anomalous: str = Field(sa_column=Column(Text(),nullable=False))
    anomalous_summary: str = Field(sa_column=Column(Text(),nullable=False))
    region_caption: str = Field(sa_column=Column(Text(),nullable=True))
    region_caption_summary: str = Field(sa_column=Column(Text(),nullable=False))
    image_time: str
    time_series: int = 1
    deleted: int = 0


class CharacterInput(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        '''
        - ombot_id (int): required Ombot id.
        - character (str): required character.
        '''
        super().__init__(**data)

    ombot_id: int
    character: str
    traits: str = "作为一个Om机器人，我喜欢观察,会经常思考下一步需要看到\
                  什么才能保障这个场景顺利进行没有故障或者危险，我喜欢提出\
                  我的意见"
    status: str = ''


class EventInput(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        '''
        - ombot_id (int): required Ombot id.
        - event (EventObject): required event.
        - source (str): optional event source ['init', 'decision'] defualt: 'decision'.
        '''
        super().__init__(**data)

    ombot_id: int
    event: EventObject
    source: str = "decision"


class MemoryInput(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        '''
        - ombot_id (int): required Ombot id.
        - memory (str): required total summary memory.
        - od_result (List[DetObject]):optional od results Object.
        - od_result_summary (str):optional od results summary.
        - caption (List[str]):optional full image caption.
        - caption_summary(str):optional full image caption summary.
        - anomalous (List[str]):optional anomalous event.
        - anomalous_summary(str):optional anomalous event summary.
        - region_caption (List[DetObject]):optional region image caption.
        - region_caption_summary(str):optional region image caption summary.
        - image_time (str): required The timestamp of the video frame.
        '''
        super().__init__(**data)

    ombot_id: int
    memory: str
    od_result: List[DetObject] = None
    od_result_summary: str = ''
    caption: List[str] = []
    caption_summary: str = ''
    anomalous: List[str] = []
    anomalous_summary: str = ''
    region_caption: List[DetObject] = None
    region_caption_summary: str = ''
    image_time: str
