from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    api_key: str
    app_name: str = "My API"

    class Config:
        env_file = ".env"


settings = Settings()