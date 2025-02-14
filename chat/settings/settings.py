from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
