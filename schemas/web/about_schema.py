from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class About(BaseModel):
    id: int
    title: str
    image_url: str
    content: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'image_url':'string',
                'content':'string',
            }
        }
    }

class AboutCreateSchema(BaseModel):
    title: str
    image_url: str
    content: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'title':'string',
                'image_url':'string',
                'content':'string',
            }
        }
    }

class AboutResponseSchema(AboutCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'image_url':'string',
                'content':'string',
            }
        }
    }

