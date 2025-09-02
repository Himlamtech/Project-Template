from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    env: str = Field(default="dev")
    log_level: str = Field(default="INFO")

    # LLM / Embeddings
    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"

    # DB
    database_url: str | None = None  # e.g., postgres+psycopg://user:pass@host/db

    model_config = {"env_file": ".env", "extra": "ignore"}


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
