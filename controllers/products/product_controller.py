from services.products.product_service import product_service
from schemas.products.product_schema import ProductCreateSchema
from fastapi import HTTPException

async def create_controller(data: ProductCreateSchema):
    return await product_service.create(data)

async def get_all_controller():
    return await product_service.get_all()

async def get_controller(id: int):
    product = await product_service.get_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def update_controller(id: int, data: ProductCreateSchema):
    product = await product_service.update(id, data)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product

async def delete_controller(id: int):
    product = await product_service.delete(id)
    if product is None:
        raise HTTPException(status_code=404, detail='not found')
    return product