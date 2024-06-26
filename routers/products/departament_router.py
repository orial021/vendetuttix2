from typing import List
from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.products.departament_schema import DepartamentCreateSchema, DepartamentResponseSchema
from controllers.products.departament_controller import create_controller, get_all_controller, get_controller, update_controller, delete_controller
from routers.user.auth_router import require_admin

departament_router = APIRouter()

@departament_router.get('/all', tags=['Departament'], response_model=List[DepartamentResponseSchema])
async def all():
    return await get_all_controller()

@departament_router.get('/show/{id}', tags=['Departament'], response_model=DepartamentResponseSchema)
async def show(id: int):
    return await get_controller(id)

@departament_router.post('/create', tags=['Departament'], response_model=DepartamentResponseSchema)
async def creater(data: DepartamentCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_controller(data)

@departament_router.put('/update/{id}', tags=['Departament'], response_model=DepartamentResponseSchema)
async def updater(id: int, data: DepartamentCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_controller(id, data)

@departament_router.delete('/delete/{id}', tags=['Departament'], response_model=DepartamentResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_controller(id)