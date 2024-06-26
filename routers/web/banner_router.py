from typing import List
from fastapi import APIRouter, Depends, Security
from models.user_model import User
from schemas.web.banner_schema import BannerCreateSchema, BannerResponseSchema
from controllers.web.banner_controller import create_banner, get_all_banners, get_banner, update_banner, delete_banner
from routers.user.auth_router import oauth2_scheme, require_admin

banner_router = APIRouter()

@banner_router.get('/all', tags=['Banner'], response_model=List[BannerResponseSchema])
async def all():
    return await get_all_banners()

@banner_router.get('/show/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def show(id: int):
    banner = await get_banner(id)
    return banner

    return templates.TemplateResponse("home.html", {"request": request, "banner": banner})

@banner_router.post('/create', tags=['Banner'], response_model=BannerResponseSchema)
async def creater(data: BannerCreateSchema, admin_user: User = Depends(require_admin)):
    return await create_banner(data)

@banner_router.put('/update/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def updater(id: int, data: BannerCreateSchema, admin_user: User = Depends(require_admin)):
    return await update_banner(id, data)

@banner_router.delete('/delete/{id}', tags=['Banner'], response_model=BannerResponseSchema)
async def deleter(id: int, admin_user: User = Depends(require_admin)):
    return await delete_banner(id)