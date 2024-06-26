from fastapi import HTTPException
from schemas.user.user_schema import UserCreateSchema
from models.user_model import User
from services.user.user_service import UserService

class user_controller:
    def __init__(self):
        self.service = UserService(User, UserCreateSchema)

    async def create_user(self, data: UserCreateSchema):
        return await self.service.create(data)

    async def get_all_users(self):
        return await self.service.get_all()

    async def get_user(self, id: int):
        user = await self.service.get_by_id(id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return user

    async def update_user(self, id: int, data: UserCreateSchema):
        user = await self.service.update(id, data)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return user

    async def delete_user(self, id: int):
        user = await self.service.delete(id)
        if user is None:
            raise HTTPException(status_code=404, detail='User not found')
        return user


user_controller = user_controller()
