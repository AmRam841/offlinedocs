from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn, computed_field

class Settings(BaseSettings):
    DB_USER: str = "offline_admin"
    DB_PASSWORD: str = "securepath"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "offlinedocs"
    
    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        # We build the Async Postgres URL automatically
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

settings = Settings()