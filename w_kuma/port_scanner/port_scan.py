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
import json


class PortScanner(object):
    def __init__(self, ipinfo, portinfo):
        self.ipinfo = ipinfo
        self.portinfo = portinfo
        self.__work_dir = os.path.dirname(os.path.abspath(__file__))
        self.__masscan_program = os.path.join(self.__work_dir, "port_resource",
                                              "masscan") if not masscan_bin else masscan_bin
        self.__outfile = "portscan_{time}.json".format(time=int(time.time()))
        self.datas = []

    @staticmethod
    def __cut_data(line):
        line = line.strip()
        if line.endswith(","):
            line = line[:-1]
            return json.loads(line)

    def __parse_masscan_outfile(self):
        temp = []
        with open("test.json", "r", encoding="utf-8") as f:
            source_data = f.readlines()
        for line in source_data:
            line = self.__cut_data(line)
            if not line:
                continue
            temp.append(
                {
                    "ip": line.get("ip"),
                    "port": line.get("ports")[0].get("port"),
                    "proto": line.get("ports")[0].get("proto"),
                    "status": line.get("ports")[0].get("status")
                }
            )
        return temp

    def portscan(self):
        if not os.path.exists(self.__masscan_program):
            print("请先安装masscan")
            return
        cmd = "{masscan} -p {portinfo} {ipinfo} --rate={rate} -oJ {outfile}".format(
            masscan=self.__masscan_program, portinfo=self.portinfo, ipinfo=self.ipinfo, rate=masscan_scan_rate,
            outfile=self.__outfile)
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
                result = self.__parse_masscan_outfile()
                self.datas = result
                return
            # 进程仍在运行
            elif ProcessStatus(process_status).status == ProcessStatusEnum.Running:
                time.sleep(1)
                continue
            # 其他异常
            else:
                return

    def run(self):
        self.portscan()


def main(ipinfo="127.0.0.1", portinfo="1-1024"):
    p = PortScanner(ipinfo=ipinfo, portinfo=portinfo)
    p.run()
    print(json.dumps(p.datas))


if __name__ == '__main__':
    main()
