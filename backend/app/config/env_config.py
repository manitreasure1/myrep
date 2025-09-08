
from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvConfig(BaseSettings):
    SECRET_KEY: str 
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_HOURS: int
    REFRESH_TOKEN_EXPIRE_DAYS: int

    SQLMODEL_ASYNC = False
    SQLMODEL_AUTO_CREATE = True,

    SQLMODEL_ECHO = True

    model_config = SettingsConfigDict(
        env_file = "./.env",
        extra='ignore'
    )