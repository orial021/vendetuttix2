from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Contact(BaseModel):
    id : int
    user_id : int
    name: str
    email : Optional[str]
    phone : Optional[str]
    subject : str
    message : str
    
    
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'user_id' : 15,
                'name' : 'pedro',
                'email' : 'pedro@mapache.com',
                'phone' : '+58 414 1234567',
                'subject' : 'titulo de la duda del cliente',
                'message' : 'duda del cliente'
                
            }
        }
    }

class ContactCreateSchema(BaseModel):
    user_id : int
    name: str
    email : Optional[str]
    phone : Optional[str]
    subject : str
    message : str
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'user_id' : 15,
                'name' : 'pedro',
                'email' : 'pedro@mapache.com',
                'phone' : '+58 414 1234567',
                'subject' : 'titulo de la duda del cliente',
                'message' : 'duda del cliente'
                
            }
        }
    }
    
    
class ContactResponseSchema(ContactCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'user_id' : 15,
                'name' : 'pedro',
                'email' : 'pedro@mapache.com',
                'phone' : '+58 414 1234567',
                'subject' : 'titulo de la duda del cliente',
                'message' : 'duda del cliente'
                
            }
        }
    }