import logging
import os
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    # app config
    DEBUG: bool = False
    PORT: int
    ENABLE_APIDOCS: bool

    LOG_TO_FILE: bool = False
    LOG_LEVEL: int = logging.DEBUG

    CORS_ALLOW_ORIGINS: str = '*'
    CORS_ALLOW_METHODS: str = '*'
    CORS_ALLOW_HEADERS: str = '*'

    # Redis
    REDIS_HOST: str
    REDIS_PREFIX: str = 'watchlist'
    REDIS_DEFAULT_TIMEOUT: int = 1 * 60 * 60
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_USERNAME: str = None
    REDIS_PASSWORD: str = None

    # Database
    DB: str
    DB_POOL_RECYCLE: int = 1800
    DB_POOL_SIZE: int = 20
    DB_POOL_PRE_PING: bool = True
    DB_ECHO: bool = False
    DB_TIMEOUT: int = 10

    # themoviedb env
    API_KEY: str
    ACCESS_TOKEN: str

    class Config:
        env_file = os.environ.get('ENV_FILE', '.env')

@lru_cache()
def get_config():
    return Settings()

settings = get_config()
