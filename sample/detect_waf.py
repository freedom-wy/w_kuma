import sys
import os
from concurrent.futures.thread import ThreadPoolExecutor
import subprocess


class HandleWafw00f(object):
    def __init__(self):
        self.wafw00f_path = self.__wafw00f_path()

    def __wafw00f_path(self):
        if self.__is_venv():
            wafw00f_path = os.path.join(os.path.dirname(sys.executable), "wafw00f")
        else:
            wafw00f_path = "/usr/local/bin/wafw00f"
        return wafw00f_path

    @staticmethod
    def __is_venv():
        return hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)

    def detech(self, url, filename):
        subprocess.Popen(
            args="{wafw00f} {url} -o {outfile}.json".format(wafw00f=self.wafw00f_path, url=url, outfile=filename),
            shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    def do(self):
        url_list = [
            {"filename": "baidu", "url": "https://www.baidu.com"},
            {"filename": "ichunqiu", "url": "https://bbs.ichunqiu.com"},
            {"filename": "venustech", "url": "https://www.venustech.com.cn"},
            {"filename": "yase", "url": "https://www.yase.me"}
        ]
        with ThreadPoolExecutor() as pool:
            future_list = [pool.submit(self.detech, item.get("url"), item.get("filename")) for item in url_list]
            for future in future_list:
                print(future.result())


if __name__ == '__main__':
    w = HandleWafw00f()
    w.do()
