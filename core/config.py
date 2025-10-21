# core/config.py
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional

BASE_DIR = Path(__file__).parent

class Settings(BaseSettings):
    DB_ENGINE: str = "mongodb"  # "mongodb" o "postgresql"

    # Mongo
    MONGODB_URI_DEV_LAB_TEST: Optional[str] = None
    MONGODB_NAME: Optional[str] = None

    # Postgres (SQLModel / SQLAlchemy async)
    POSTGRES_URI: Optional[str] = None

    # App
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_DESCRIPTION: str = "Plantilla FastAPI con MongoDB y Postgres (SQLModel)."
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:4321", "https://lims-qc-ui.vercel.app"]

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / "config.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
