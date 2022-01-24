"""
端口扫描
1、调用masscan扫描开放端口
2、调用nmap识别端口开放服务
"""

import os
import time
from w_kuma.config import *
import subprocess
from w_kuma.libs.process_utils import ProcessStatus, ProcessStatusEnum


class PortScanner(object):
    def __init__(self, ipinfo, portinfo):
        self.ipinfo = ipinfo
        self.portinfo = portinfo
        self.__work_dir = os.path.dirname(os.path.abspath(__file__))
        self.__masscan_program = os.path.join(self.__work_dir, "port_resource", "masscan")
        self.__outfile = "portscan_{time}.xml".format(time=int(time.time()))

    def __parse_masscan_outfile(self):
        pass

    def portscan(self):
        cmd = "{masscan} -p {portinfo} {ipinfo} --rate={rate} -oX {outfile}".format(
            masscan=self.__masscan_program, portinfo=self.portinfo, ipinfo=self.ipinfo, rate=masscan_scan_rate, outfile=self.__outfile)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        # 判断masscan进程状态
        while True:
            process_status = process.poll()
            # 进程不存在
            if isinstance(process_status, int) and process_status > ProcessStatusEnum.End.value:
                stdout, stderr = process.communicate()
                print(stderr)
                return
            # 进程正常结束退出
            elif ProcessStatus(process_status).status == ProcessStatusEnum.End:
                # 处理masscan扫描结果文件
                break
            # 进程仍在运行
            elif ProcessStatus(process_status).status == ProcessStatusEnum.Running:
                time.sleep(1)
                continue
            # 异常退出
            else:
                pass

    def run(self):
        pass


def main(ipinfo="127.0.0.1", portinfo="1-1024"):
    p = PortScanner(ipinfo=ipinfo, portinfo=portinfo)
    p.portscan()


if __name__ == '__main__':
    main()
