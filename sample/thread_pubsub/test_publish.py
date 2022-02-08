from handle_pubsub import Publisher
import json

redis_publish = Publisher(channels="test1")
redis_publish.publish(json.dumps({"name": "haha"}))
