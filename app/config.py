from pydantic import Field
from pydantic_settings import BaseSettings
from functools import lru_cache


@lru_cache()
def get_settings():
    settings = SensitiveSettings(_env_file=".env", _env_file_encoding="utf-8")
    return settings


class MainSettings(BaseSettings):
    ...


class EnvironmentSettings(MainSettings):
    ...


class SensitiveSettings(EnvironmentSettings):
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


APP_SETTINGS = get_settings()
