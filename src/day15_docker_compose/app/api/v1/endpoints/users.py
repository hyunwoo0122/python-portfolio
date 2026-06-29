from fastapi import APIRouter
from app.schemas.user import UserResponse, UserCreateRequest

router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreateRequest):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
    }