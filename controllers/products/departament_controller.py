from services.products.departament_service import departament_service
from schemas.products.departament_schema import DepartamentCreateSchema
from fastapi import HTTPException

async def create_controller(data: DepartamentCreateSchema):
    return await departament_service.create(data)

async def get_all_controller():
    return await departament_service.get_all()

async def get_controller(id: int):
    departament = await departament_service.get_by_id(id)
    if departament is None:
        raise HTTPException(status_code=404, detail='not found')
    return departament

async def update_controller(id: int, data: DepartamentCreateSchema):
    departament = await departament_service.update(id, data)
    if departament is None:
        raise HTTPException(status_code=404, detail='not found')
    return departament

async def delete_controller(id: int):
    departament = await departament_service.delete(id)
    if departament is None:
        raise HTTPException(status_code=404, detail='not found')
    return departament