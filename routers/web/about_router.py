from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.web.about_schema import AboutCreateSchema, AboutResponseSchema
from controllers.web.about_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

about_router = APIRouter()

@about_router.get('/all', tags=['About'], response_model=List[AboutResponseSchema])
async def all():
    return await get_all_controller()

@about_router.get('/show/{id}', tags=['About'], response_model=AboutResponseSchema)
async def show(id: int):
    return await get_controller(id)

@about_router.post('/create', tags=['About'], response_model=AboutResponseSchema)
async def creater(data: AboutCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@about_router.put('/update/{id}', tags=['About'], response_model=AboutResponseSchema)
async def updater(id: int, data: AboutCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@about_router.delete('/delete/{id}', tags=['About'], response_model=AboutResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)