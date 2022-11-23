from fastapi import APIRouter

from api.v1.api import api_routers
from core.config import settings

root_router = APIRouter()

root_router.include_router(api_routers, prefix=settings.API_V1_STR)