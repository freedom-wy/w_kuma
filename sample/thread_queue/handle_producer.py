from handle_queue import RedisQueue


class Producer(RedisQueue):
    def __init__(self, keys):
        RedisQueue.__init__(self)
        self.keys = keys

    def do(self):
        for i in range(1, 6):
            self.rpush(keys=self.keys, data=i)


if __name__ == '__main__':
    p = Producer(keys="test1")
    p.do()
