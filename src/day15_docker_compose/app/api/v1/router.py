from fastapi import APIRouter
from app.api.v1.endpoints import items,users

router = APIRouter()

router.include_router(items.router)
router.include_router(users.router)