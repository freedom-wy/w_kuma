from redis_lib import check_redis_connect


class RedisQueue(object):
    def __init__(self, redis_connect=None):
        self.redis_connect = check_redis_connect(redis_connect)
