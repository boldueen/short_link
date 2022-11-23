import logging
import pathlib
import sys
import os
import dotenv
from typing import List

from loguru import logger
from pydantic import BaseSettings, AnyHttpUrl

from core.logging import InterceptHandler

ROOT = pathlib.Path(__file__).resolve().parent.parent
dotenv_path = ("../../.env")

dotenv.load_dotenv(dotenv.find_dotenv())


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    API_V2_STR: str = "/api/v2"
    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    ALGORITHM: str = "HS256"
    MAIL_EMAIL: str = os.environ.get("EMAIL")
    MAIL_PASS: str = os.environ.get("PASS")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    logging: LoggingSettings = LoggingSettings()


    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


def setup_app_logging(config: Settings) -> None:
    """Custom logging for application"""
    LOGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

    logger.configure(
        handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
    )


settings = Settings()