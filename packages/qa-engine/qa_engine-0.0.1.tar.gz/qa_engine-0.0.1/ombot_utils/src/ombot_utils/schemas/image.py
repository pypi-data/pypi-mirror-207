from typing import List, Dict, Any, Union
from pydantic import BaseModel



class ImageSrc(BaseModel):
    src_type: str
    data: str
    image_file: Any = None
    event_time: str
    video_id: str = ''
    Image_id: str = ''
    kwargs: Dict = {}
        
class FrameRequest(BaseModel):
    bot_id:str
    callback: str
    src: List[ImageSrc]
    
    def __len__(self):
        return len(self.src)

    def __iter__(self):
        return iter(self.src)

    def __getitem__(self, key):
        return self.src[key]

    def __setitem__(self, key, value):
        assert isinstance(value, ImageSrc)
        self.src[key] = value
