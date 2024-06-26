from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.web.contact_schema import ContactCreateSchema, ContactResponseSchema
from controllers.web.contact_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

contact_router = APIRouter()

@contact_router.get('/all', tags=['Contact'], response_model=List[ContactResponseSchema])
async def all():
    return await get_all_controller()

@contact_router.get('/show/{id}', tags=['Contact'], response_model=ContactResponseSchema)
async def show(id: int):
    return await get_controller(id)

@contact_router.post('/create', tags=['Contact'], response_model=ContactResponseSchema)
async def creater(data: ContactCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@contact_router.put('/update/{id}', tags=['Contact'], response_model=ContactResponseSchema)
async def updater(id: int, data: ContactCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@contact_router.delete('/delete/{id}', tags=['Contact'], response_model=ContactResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)