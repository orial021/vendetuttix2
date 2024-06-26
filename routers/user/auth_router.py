from typing import Annotated
from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from models.user_model import User
import os
from schemas.user.user_schema import RoleEnum



auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

secret_key = os.getenv("SECRET_KEY")

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

async def decode_token(token: str =  Depends(oauth2_scheme)) -> dict:
    try:
        data = jwt.decode(token, secret_key, algorithms= ['HS256'])
        user = await User.get(username=data['username'])
        if user is None:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                                detail = 'Invalid authentication credentials',
                                headers = { 'WWW-Authenticate': 'Bearer'})
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid token",
                            headers={"WWW-Authenticate": "Bearer"})

def require_admin(user: User = Depends(decode_token)):
    if user.rol != RoleEnum.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You don't have permission to access this resource")
    return user

async def get_user_id(user: User = Depends(decode_token)):
    return user.id

@auth_router.post('/login', tags=['Auth'])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await User.get_or_none(username=form_data.username)
    if not user or form_data.password != user.password:
        raise HTTPException(status_code=400, detail='Credenciales inválidas')
    token = encode_token({"username": user.username, "email": user.email})
    return { 'access_token': token }

@auth_router.get('/profile', tags=['Auth'])
async def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return my_user
