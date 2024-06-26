from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
import uuid

from enum import Enum

class RoleEnum(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class User(BaseModel):
    id : uuid.UUID
    username : str
    password : str
    email : EmailStr
    name : str
    rol : RoleEnum
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'username' : 'usuario1',
                'password' : '123456',
                'email' : 'usuario@12345.com',
                'name' : 'nombre de usuario',
                'rol' : 'client'
            }
        }
    }

class UserCreateSchema(BaseModel):
    username : str
    password : str
    email : EmailStr
    name : str
    rol : RoleEnum
    

    
    model_config = {
        'json_schema_extra':{
            'example':{
                'username' : 'usuario1',
                'password' : '123456',
                'email' : 'usuario@12345.com',
                'name' : 'nombre de usuario',
                'rol' : 'client'
            }
        }
    }
    
    
class UserResponseSchema(UserCreateSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    

    
    model_config = {
        'json_schema_extra':{
            'example':{
                'id': 1,
                'username' : 'usuario1',
                'password' : '123456',
                'email' : 'usuario@12345.com',
                'name' : 'nombre de usuario',
                'rol' : 'client'
            }
        }
    }