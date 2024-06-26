from services.web.reviews_service import reviews_service
from schemas.web.reviews_schema import ReviewsCreateSchema
from fastapi import HTTPException

async def create_controller(data: ReviewsCreateSchema, user_id : int):
    data_dict = data.model_dump()
    data_dict['user_id'] = user_id
    print(data_dict)
    return await reviews_service.create(data_dict)

async def get_all_controller():
    return await reviews_service.get_all()

async def get_controller(id: int):
    reviews = await reviews_service.get_by_id(id)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

async def get_by_user(user_id : int):
    reviews = await reviews_service.get_by_user(user_id)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

async def update_controller(id: int, data: ReviewsCreateSchema):
    reviews = await reviews_service.update(id, data)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

async def delete_controller(id: int):
    reviews = await reviews_service.delete(id)
    if reviews is None:
        raise HTTPException(status_code=404, detail='not found')
    return reviews

