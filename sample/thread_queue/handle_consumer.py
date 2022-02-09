import threading

from handle_queue import RedisQueue
from concurrent.futures.thread import ThreadPoolExecutor
import time


class Consumer(RedisQueue):
    def __init__(self, name, keys="test1"):
        RedisQueue.__init__(self, name)
        self.keys = keys
        self.thread_name = name

    @staticmethod
    def handle_data(data):
        time.sleep(20)
        return data

    def get_result(self, future):
        print("{}最终结果为: {}".format(self.thread_name, future.result()))

    def run(self):
        # 通过多线程处理队列中数据
        with ThreadPoolExecutor() as pool:
            while True:
                keys, data = self.blpop(keys=self.keys)
                print("{}从队列中取出的数据为: {}".format(self.thread_name, data.decode()))
                future = pool.submit(self.handle_data, data.decode())
                future.add_done_callback(self.get_result)


if __name__ == '__main__':
    thread_list = [Consumer(name="线程: {}号".format(i)) for i in range(1, 3)]
    for i in thread_list:
        i.start()
