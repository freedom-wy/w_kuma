import redis
from error import NoChannelError
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB


def check_redis_connect(redis_connect):
    if not redis_connect:
        redis_connect = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)
    return redis_connect


def check_channels(channels):
    if not channels:
        raise NoChannelError("未订阅频道")
    return channels

