from handle_queue import RedisQueue


class Producer(RedisQueue):
    def __init__(self, keys, name):
        RedisQueue.__init__(self, name)
        self.keys = keys

    def run(self):
        for i in range(1, 101):
            self.rpush(keys=self.keys, data=i)


if __name__ == '__main__':
    p = Producer(keys="test1", name="生产者")
    p.start()
