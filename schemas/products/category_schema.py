from enum import Enum
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Category(BaseModel):
    id: int
    title: str
    description: str
    departament_id: str
    departaments: str
    is_active: bool
    image_url: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'description':'string',
                'departament_id':'string',
                'departaments':'string',
                'is_active':'True',
                'image_url':'string',
            }
        }
    }

class CategoryCreateSchema(BaseModel):
    title: str
    description: str
    departament_id: str
    departaments: str
    is_active: bool
    image_url: str


    model_config = { 
       'json_schema_extra':{
            'example':{
                'title':'string',
                'description':'string',
                'departament_id':'string',
                'departaments':'string',
                'is_active':'True',
                'image_url':'string',
            }
        }
    }

class CategoryResponseSchema(CategoryCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None


    model_config = { 
       'json_schema_extra':{
            'example':{
                'id':1,
                'title':'string',
                'description':'string',
                'departament_id':'string',
                'departaments':'string',
                'is_active':'True',
                'image_url':'string',
            }
        }
    }

