from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Content(BaseModel):
    id : int
    title : str
    description : str
    url : Optional[str]
    image_url : Optional[str]
    
    
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'url' : 'www.urlcontent.com',
                'image_url': 'imagen1.jpg',
            }
        }
    }

class ContentCreateSchema(BaseModel):
    title: str
    image_url: str
    description: str
    url : str | None = None
    image_url : str | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'title' : 'Content1',
                'description' : 'description',
                'url' : 'www.urlcontent.com',
                'image_url': 'imagen1.jpg',
            }
        }
    }
    
class ContentResponseSchema(ContentCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'url' : 'www.urlcontent.com',
                'image_url': 'imagen1.jpg',
            }
        }
    }