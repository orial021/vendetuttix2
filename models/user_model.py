from tortoise import fields
from tortoise.models import Model
from schemas.user.user_schema import RoleEnum, User
import uuid
import bcrypt

def hash_password(plain_password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed_password.decode()


class User(Model):
    id = fields.UUIDField(pk=True, default = uuid.uuid4)
    username = fields.CharField(max_length=30)
    password = fields.CharField(max_length=60)
    email = fields.CharField(max_length=30, unique=True)
    name = fields.TextField(max_length=30)
    rol = fields.CharEnumField(RoleEnum)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    deleted_at = fields.DatetimeField(null = True)
    

    def __str__(self):
        return self.username
    
    class Meta:
        table = "user"
