from services.web.content_service import content_service
from schemas.web.content_schema import ContentCreateSchema
from fastapi import HTTPException

async def create_controller(data: ContentCreateSchema):
    return await content_service.create(data)

async def get_all_controller():
    return await content_service.get_all()

async def get_controller(id: int):
    content = await content_service.get_by_id(id)
    if content is None:
        raise HTTPException(status_code=404, detail='not found')
    return content

async def update_controller(id: int, data: ContentCreateSchema):
    content = await content_service.update(id, data)
    if content is None:
        raise HTTPException(status_code=404, detail='not found')
    return content

async def delete_controller(id: int):
    content = await content_service.delete(id)
    if content is None:
        raise HTTPException(status_code=404, detail='not found')
    return content
