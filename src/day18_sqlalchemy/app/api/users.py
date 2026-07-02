from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.crud.user import (
    create_user,
    delete_user,
    get_user,
    update_user,
)
from app.schemas.user import (
    UserCreateRequest,
    UserResponse,
)

router = APIRouter()


@router.post("/users", response_model=UserResponse)
async def create(
    user: UserCreateRequest,
    db: AsyncSession = Depends(get_db),
):
    return await create_user(db, user)


@router.get("/users/{user_id}", response_model=UserResponse)
async def read(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    user = await get_user(db, user_id)

    if user is None:
        raise HTTPException(404, "User not found")

    return user


@router.put("/users/{user_id}", response_model=UserResponse)
async def update(
    user_id: int,
    user_data: UserCreateRequest,
    db: AsyncSession = Depends(get_db),
):
    user = await update_user(
        db,
        user_id,
        user_data,
    )

    if user is None:
        raise HTTPException(404, "User not found")

    return user


@router.delete("/users/{user_id}")
async def delete(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    user = await delete_user(db, user_id)

    if user is None:
        raise HTTPException(404, "User not found")

    return {"message": "삭제 완료"}