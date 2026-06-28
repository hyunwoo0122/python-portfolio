from pydantic import BaseModel, Field, EmailStr

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