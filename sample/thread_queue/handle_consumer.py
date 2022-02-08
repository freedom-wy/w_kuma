from handle_queue import RedisQueue
from concurrent.futures.thread import ThreadPoolExecutor
import time


class Consumer(RedisQueue):
    def __init__(self, keys):
        RedisQueue.__init__(self)
        self.keys = keys

    @staticmethod
    def handle_data(data):
        time.sleep(int(data))
        return data

    @staticmethod
    def get_result(future):
        print("最终结果为: {}".format(future.result()))

    def do(self):
        # 通过多线程处理队列中数据
        with ThreadPoolExecutor() as pool:
            while True:
                keys, data = self.blpop(keys=self.keys)
                print("从队列中取出的数据为: {}".format(data.decode()))
                future = pool.submit(self.handle_data, data.decode())
                future.add_done_callback(self.get_result)


if __name__ == '__main__':
    c = Consumer(keys="test1")
    c.do()
