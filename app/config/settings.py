from pydantic import Field
from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    DB_HOST: str = Field(default="localhost")
    DB_PORT: int = Field(default=5432)
    DB_USER: str = Field(default="postgres")
    DB_PASS: str = Field(default="postgres")
    DB_NAME: str = Field(default="postgres")
