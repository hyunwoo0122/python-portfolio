from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.users import router
from app.core.database import engine
from app.models.user import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)