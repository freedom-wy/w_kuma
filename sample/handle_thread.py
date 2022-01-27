# import threading
# import time

# # 最大线程数
# max_thread = 2
# semaphore = threading.BoundedSemaphore(max_thread)
#
#
# # 多线程
# class TestThread(threading.Thread):
#     def __init__(self, name, value):
#         threading.Thread.__init__(self, name=name)
#         self.value = value
#         self.name = name
#         self.result = 0
#
#     def run(self):
#         # 限定最大线程数
#         with semaphore:
#             print("{}号线程执行数据: {}".format(self.name, self.value))
#             # time.sleep(2)
#             for i in range(10):
#                 self.result += 1
#
#     # 获取线程返回值
#     def get_result(self):
#         return "{}号线程执行结果: {}".format(self.name, self.result)
#
#
# thread_list = [TestThread(name="kuma-{}".format(i), value=i) for i in range(10)]
# for i in thread_list:
#     i.start()
# for i in thread_list:
#     i.join()
# for i in thread_list:
#     print(i.get_result())

# # 多线程共享变量造成的线程内部数据混乱
# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(1000000):
#         with lock:
#             change_it(n)
#
#
# t1 = threading.Thread(target=run_thread, args=(100,))
# t2 = threading.Thread(target=run_thread, args=(200,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
# 线程池
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, FIRST_COMPLETED
import threading
import time


def test(max_value):
    my_sum = 0
    print("{}号线程".format(threading.current_thread().name))
    for i in range(max_value):
        my_sum = my_sum + 1
        time.sleep(1)
    return my_sum


def get_result(future):
    print(future.result())


# # 线程池限制为2
# with ThreadPoolExecutor(max_workers=2) as pool:
#     # 单独提交线程方式
#     future1 = pool.submit(test, 10)
#     future2 = pool.submit(test, 10)
#     # # pool.shutdown()  # 执行线程池关闭后新的线程将无法提交
#     # # 当线程池中有空闲线程时会提交第三个线程
#     # future3 = pool.submit(test, 10)
#     # while True:
#     #     if future3.done():
#     #         print(future3.result())
#     #         break
#     #     else:
#     #         continue
#     # 添加回调方法,回调方法不会阻塞
#     future1.add_done_callback(get_result)
#     print("主程序")
# 并发提交线程
# with ThreadPoolExecutor() as pool:
#     results = pool.map(test, [10, 20, 30])
#     for i in results:
#         print(i)
value_list = [10, 20, 30]
with ThreadPoolExecutor() as pool:
    # submit返回的是future,Future 实例由 Executor.submit() 创建
    # future_list = [pool.submit(test, i) for i in value_list]
    # for future in concurrent.futures.as_completed(future_list):
    #     print(future.result())
    future_list = [pool.submit(test, i) for i in value_list]
    # 可以设置什么时候返回数据ALL_COMPLETED或FIRST_COMPLETED
    concurrent.futures.wait(future_list, return_when=FIRST_COMPLETED)
    for future in concurrent.futures.as_completed(future_list):
        print(future.result())
    # map返回的是结果
    # results = pool.map(test, value_list)
    # for i in results:
    #     print(i)



