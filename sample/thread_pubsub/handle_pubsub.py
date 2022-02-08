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


# 订阅者
class Subscriber(object):
    def __init__(self, redis_connect=None, channels=None):
        self.redis_connect = check_redis_connect(redis_connect)
        self.channels = check_channels(channels)
        self.pubsub = self.redis_connect.pubsub()
        # 订阅频道
        self.pubsub.subscribe(self.channels)


# 发布者
class Publisher(object):
    def __init__(self, redis_connect=None, channels=None):
        self.redis_connect = check_redis_connect(redis_connect)
        self.channels = check_channels(channels)

    def publish(self, message):
        self.redis_connect.publish(channel=self.channels, message=message)


if __name__ == '__main__':
    pass
