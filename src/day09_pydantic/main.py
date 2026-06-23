from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()


class UserCreateRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=50,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
    )


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreateRequest):
    return {
        "id": 1,
        "name": user.name,
        "email": user.email,
        "password": user.password,
    }