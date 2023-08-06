from pydantic import BaseModel
from typing import Any


class Response(BaseModel):
    took: float
    msg: Any
    code: int
    result: dict

