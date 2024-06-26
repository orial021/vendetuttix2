from typing import List
from fastapi import APIRouter, Depends, Security
from models.user_model import User
from schemas.web.content_schema import ContentCreateSchema, ContentResponseSchema
from controllers.web.content_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import oauth2_scheme, require_admin

content_router = APIRouter()

@content_router.get('/all', tags=['Content'], response_model=List[ContentResponseSchema])
async def all():
    return await get_all_controller()

@content_router.get('/show/{id}', tags=['Content'], response_model=ContentResponseSchema)
async def show(id: int):
    return await get_controller(id)

@content_router.post('/create', tags=['Content'], response_model=ContentResponseSchema)
async def creater(data: ContentCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@content_router.put('/update/{id}', tags=['Content'], response_model=ContentResponseSchema)
async def updater(id: int, data: ContentCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@content_router.delete('/delete/{id}', tags=['Content'], response_model=ContentResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)