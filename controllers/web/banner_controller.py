from services.web.banner_service import banner_service
from schemas.web.banner_schema import BannerCreateSchema
from fastapi import HTTPException

async def create_banner(data: BannerCreateSchema):
    return await banner_service.create(data)

async def get_all_banners():
    return await banner_service.get_all()

async def get_banner(id: int):
    banner = await banner_service.get_by_id(id)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner

async def update_banner(id: int, data: BannerCreateSchema):
    banner = await banner_service.update(id, data)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner

async def delete_banner(id: int):
    banner = await banner_service.delete(id)
    if banner is None:
        raise HTTPException(status_code=404, detail='not found')
    return banner
