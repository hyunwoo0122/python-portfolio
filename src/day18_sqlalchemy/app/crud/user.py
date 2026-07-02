from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreateRequest


async def create_user(
    db: AsyncSession,
    user_data: UserCreateRequest,
):
    new_user = User(
        name=user_data.name,
        email=user_data.email,
    )

    db.add(new_user)

    await db.commit()

    await db.refresh(new_user)

    return new_user


async def get_user(
    db: AsyncSession,
    user_id: int,
):
    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    return result.scalar_one_or_none()


async def update_user(
    db: AsyncSession,
    user_id: int,
    user_data: UserCreateRequest,
):
    user = await get_user(db, user_id)

    if user is None:
        return None

    user.name = user_data.name
    user.email = user_data.email

    await db.commit()

    await db.refresh(user)

    return user


async def delete_user(
    db: AsyncSession,
    user_id: int,
):
    user = await get_user(db, user_id)

    if user is None:
        return None

    await db.delete(user)

    await db.commit()

    return user