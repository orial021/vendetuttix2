from services.products.category_service import category_service
from schemas.products.category_schema import CategoryCreateSchema
from fastapi import HTTPException
async def create_controller(data: CategoryCreateSchema):
    return await category_service.create(data)

async def get_all_controller():
    return await category_service.get_all()

async def get_controller(id: int):
    category = await category_service.get_by_id(id)
    if category is None:
        raise HTTPException(status_code=404, detail='not found')
    return category

async def update_controller(id: int, data: CategoryCreateSchema):
    category = await category_service.update(id, data)
    if category is None:
        raise HTTPException(status_code=404, detail='not found')
    return category

async def delete_controller(id: int):
    category = await category_service.delete(id)
    if category is None:
        raise HTTPException(status_code=404, detail='not found')
    return category