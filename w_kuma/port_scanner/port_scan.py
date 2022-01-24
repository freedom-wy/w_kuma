"""
端口扫描
1、调用masscan扫描开放端口
2、调用nmap识别端口开放服务
"""

import os
import time
from w_kuma.config import *
import subprocess


class PortScanner(object):
    def __init__(self, ipinfo, portinfo):
        self.ipinfo = ipinfo
        self.portinfo = portinfo
        self.__work_dir = os.path.dirname(os.path.abspath(__file__))
        self.__masscan_program = os.path.join(self.__work_dir, "port_resource", "masscan")
        self.__outfile = "portscan_{time}.xml".format(time=int(time.time()))

    def portscan(self):
        cmd = "masscan -p {portinfo} {ipinfo} --rate={rate} -oX {outfile}".format(
            portinfo=self.portinfo, ipinfo=self.ipinfo, rate=masscan_scan_rate, outfile=self.__outfile)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # 判断masscan进程状态
