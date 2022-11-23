from fastapi import APIRouter

from api.v1.endpoints import users
from api.v1.endpoints import socials



api_routers = APIRouter()

api_routers.include_router(users.router, prefix="/user", tags=["users"])
api_routers.include_router(socials.router, prefix="/social", tags=["socials"])
