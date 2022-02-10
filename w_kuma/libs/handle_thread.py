# 多线程
from concurrent.futures.thread import ThreadPoolExecutor
from w_kuma.libs.handle_request_http import HTTP
from concurrent.futures import wait, FIRST_COMPLETED


class ThreadRequest(object):
    def __init__(self):
        self.data_list = []

    def thread_request_zoomeye_api(self, url_list: list):
        with ThreadPoolExecutor() as pool:
            future_list = [pool.submit(HTTP().get, url) for url in url_list]
            wait(future_list, return_when=FIRST_COMPLETED)
            for future in future_list:
                self.data_list.append(future.result())

