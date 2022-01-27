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
