from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Reviews(BaseModel):
    id : int
    title : str
    description : str
    rating : int
    user_id : int | None = None
    related_product : int | None = None
    
    
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'title' : 'Content1',
                'description' : 'description',
                'rating' : 4,
                'user_id' : 12,
                'related_product' : 85
            }
        }
    }

class ReviewsCreateSchema(BaseModel):
    title : str
    description : str
    rating : int
    user_id : int | None = None
    related_product : int | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'title' : 'Content1',
                'description' : 'description',
                'rating' : 4,
                'related_product' : 85
            }
        }
    }
    
    
class ReviewsResponseSchema(ReviewsCreateSchema):
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
                'rating' : 4,
                'user_id' : 12,
                'related_product' : 85
            }
        }
    }