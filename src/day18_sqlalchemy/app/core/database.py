# app/core/database.py
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.models.user import Base   # Base를 여기서 가져온다

# .env에서 읽어온 DATABASE_URL 사용 (하드코딩 제거)
engine = create_async_engine(
    settings.database_url,
    echo=True,
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# 테이블을 실제로 생성하는 함수 (새로 추가)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)