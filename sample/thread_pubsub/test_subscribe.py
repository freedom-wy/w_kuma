from handle_pubsub import Subscriber

redis_subscribe = Subscriber(channels="test1")
for item in redis_subscribe.pubsub.listen():
    if item.get("type") == "message":
        print(item.get("data").decode())
