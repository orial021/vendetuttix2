from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.products.category_schema import CategoryCreateSchema, CategoryResponseSchema
from controllers.products.category_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

category_router = APIRouter()

@category_router.get('/all', tags=['Category'], response_model=List[CategoryResponseSchema])
async def all():
    return await get_all_controller()

@category_router.get('/show/{id}', tags=['Category'], response_model=CategoryResponseSchema)
async def show(id: int):
    return await get_controller(id)

@category_router.post('/create', tags=['Category'], response_model=CategoryResponseSchema)
async def creater(data: CategoryCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@category_router.put('/update/{id}', tags=['Category'], response_model=CategoryResponseSchema)
async def updater(id: int, data: CategoryCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@category_router.delete('/delete/{id}', tags=['Category'], response_model=CategoryResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)