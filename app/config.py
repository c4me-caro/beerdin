from functools import cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=True,
        extra="allow"
    )

    DISCORD_TOKEN: SecretStr
    DB_CONNECTION: SecretStr
    MONGO_URI: SecretStr
    MONGO_DB_NAME: SecretStr

@cache
def getConfig() -> Config:
    return Config()
