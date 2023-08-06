from nonebot import get_driver
from pydantic import BaseSettings


class Config(BaseSettings):
    majsoul_query_timeout: float = 15.0

    class Config:
        extra = "ignore"


conf = Config(**get_driver().config.dict())
