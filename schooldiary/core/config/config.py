from pydantic_settings import BaseSettings, SettingsConfigDict

from .database import DataBaseConfig
from .server import ServerConfig


class AppConfig(BaseSettings):
    server: ServerConfig = ServerConfig()
    db: DataBaseConfig

    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )


conf = AppConfig()  # noqa
