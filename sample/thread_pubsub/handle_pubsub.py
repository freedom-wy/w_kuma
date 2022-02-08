from redis_lib import check_redis_connect, check_channels


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

