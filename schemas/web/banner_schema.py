from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Banner(BaseModel):
    id : int
    title : str
    image_url : str
    content : str
    status : Optional[bool]
    click_count : Optional[int]
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Banner1',
                'image_url': 'imagen1.jpg',
                'content': 'lorem ipsum',
                'status' : 'True',
                'click_count' : '10'
            }
        }
    }

class BannerCreateSchema(BaseModel):
    title: str
    image_url: str
    content: str
    status: bool | None = None 
    click_count: int | None = None
    
    
class BannerResponseSchema(BannerCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Banner1',
                'image_url': 'imagen1.jpg',
                'content': 'lorem ipsum',
                'status' : 'True',
                'click_count' : '10'
            }
        }
    }