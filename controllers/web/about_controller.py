from services.web.about_service import about_service
from schemas.web.about_schema import AboutCreateSchema
from fastapi import HTTPException

async def create_controller(data: AboutCreateSchema):
    return await about_service.create(data)

async def get_all_controller():
    return await about_service.get_all()

async def get_controller(id: int):
    about = await about_service.get_by_id(id)
    if about is None:
        raise HTTPException(status_code=404, detail='not found')
    return about

async def update_controller(id: int, data: AboutCreateSchema):
    about = await about_service.update(id, data)
    if about is None:
        raise HTTPException(status_code=404, detail='not found')
    return about

async def delete_controller(id: int):
    about = await about_service.delete(id)
    if about is None:
        raise HTTPException(status_code=404, detail='not found')
    return about