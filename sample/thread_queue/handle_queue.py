import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB


class RedisQueue(object):
    def __init__(self):
        self.redis_connect = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

    def blpop(self, keys):
        return self.redis_connect.blpop(keys=keys)

    def rpush(self, keys, data):
        return self.redis_connect.rpush(keys, data)

