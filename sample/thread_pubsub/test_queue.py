from handle_redis_queue import RedisQueue
import json


queue = RedisQueue()
print(queue.redis_connect.llen("test1"))
for i in range(1, 6):
    queue.redis_connect.rpush("test1", json.dumps({"i": i}))
print(queue.redis_connect.llen("test1"))
while True:
    key, data, = queue.redis_connect.blpop("test1")
    print(data.decode())


