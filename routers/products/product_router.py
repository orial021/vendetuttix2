from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.products.product_schema import ProductCreateSchema, ProductResponseSchema
from controllers.products.product_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

product_router = APIRouter()

@product_router.get('/all', tags=['Product'], response_model=List[ProductResponseSchema])
async def all():
    return await get_all_controller()

@product_router.get('/show/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def show(id: int):
    return await get_controller(id)

@product_router.post('/create', tags=['Product'], response_model=ProductResponseSchema)
async def creater(data: ProductCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@product_router.put('/update/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def updater(id: int, data: ProductCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@product_router.delete('/delete/{id}', tags=['Product'], response_model=ProductResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)