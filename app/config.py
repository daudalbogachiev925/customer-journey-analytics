from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:pass@db:5432/journey"
    MAX_PATH_LENGTH: int = 15
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
