from pydantic_settings import BaseSettings
from pydantic import Field


class PostgresSettings(BaseSettings):
    POSTGRES_DB: str = Field(
        default=None,
    )
    POSTGRES_USER: str = Field(
        default=None,
    )
    POSTGRES_PASSWORD: str = Field(
        default=None,
    )
