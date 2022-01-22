"""
域名扫描
1、子域名爆破
2、泛解析
3、通过api接口获取子域名

处理逻辑
1、通过泛解析ip裁剪一次数据
2、域名Ip数大于1判定为cdn
3、剩余数据为最终数据
"""

import math
import shutil
from config import *
import sys
import os
import subprocess
from multiprocessing import cpu_count
import time


class Wkuma(object):
    def __init__(self, domain):
        self.result = {}
        self.domain = domain
        # 工作目录
        self.work_dir = os.path.dirname(os.path.abspath(__file__))
        # 子域名字典目录
        self.subdomain_dict_path = os.path.join(self.work_dir, subdomain_dict_path)
        # 分割字典文件
        self.subdomain_dict_file_list = self.split_subdomain_dict_file()
        self.aiodnsbrute_temp_path = os.path.join(self.work_dir, "temp")

    def split_subdomain_dict_file(self):
        """
        分割字典文件
        :return:
        """
        tmp = []
        prefix = "split_subdomain"
        if subdomain_flag == "FULL":
            # 分割字典文件
            subdomain_dict_file = os.path.join(self.subdomain_dict_path, subdomain_filename)
            try:
                dict_lines_count = int(
                    subprocess.check_output("wc -l {}".format(subdomain_dict_file), shell=True).strip().split()[0])
            except Exception as e:
                subdomain_dict_file = os.path.join(self.subdomain_dict_path, top_subdomain_filename)
                tmp.append(subdomain_dict_file)
            else:
                cpu_num = max(cpu_count() - 1, 1)
                lines_in_each_file = math.ceil(dict_lines_count / cpu_num)
                # 分割文件
                subprocess.check_call("cd {work_dir} && rm -f {prefix}* && split -l {line_num} {raw_file} {prefix}"
                                      .format(work_dir=self.subdomain_dict_path, line_num=lines_in_each_file,
                                              raw_file=subdomain_dict_file, prefix=prefix), shell=True)
                for root, dirs, files in os.walk(self.subdomain_dict_path):
                    for file in files:
                        if file.startswith(prefix):
                            tmp.append(os.path.join(root, file))
        elif subdomain_flag == "SUB":
            # 加载top子域名文件
            subdomain_dict_top_file = os.path.join(self.subdomain_dict_path, top_subdomain_filename)
            tmp.append(subdomain_dict_top_file)
        return tmp

    def aiodnsbrute_path(self):
        """
        输出aiodnsbrute程序路径
        :return:
        """
        if self.is_venv():
            aiodnsbrute_path = os.path.join(os.path.dirname(sys.executable), "aiodnsbrute")
        else:
            aiodnsbrute_path = "/usr/local/bin/aiodnsbrute"
        return aiodnsbrute_path

    @staticmethod
    def is_venv():
        """
        判断当前环境是否为虚拟环境
        :return:
        """
        return hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)

    def subdomain_brute(self):
        """
        子域名爆破
        :return:
        """
        aiodnsbrute_process_list = []
        aiodnsbrute_result_list = []
        # 1、查找aiodnsbrute路径
        aiodnsbrute_path = self.aiodnsbrute_path()
        if not aiodnsbrute_path:
            raise ModuleNotFoundError("aiodnsbrute包未安装")
        aiodnsbrute_program = "LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 {python_interpreter} {aiodnsbrute_program}".format(
            python_interpreter=sys.executable, aiodnsbrute_program=aiodnsbrute_path)
        if not os.path.exists(self.aiodnsbrute_temp_path):
            os.mkdir(self.aiodnsbrute_temp_path)
        # aiodnsbrute执行命令
        for subdomain_dict_file in self.subdomain_dict_file_list:
            subdomain_brute_output_filename = os.path.join(self.aiodnsbrute_temp_path,
                                                           "subdomain_brute_{}".format(int(time.time())))
            aiodnsbrute_work_cmd = "{aiodnsbrute_program} -w {brute_dict} -r {dns_server_list} -f {output_file} -o json -t 5000 --no-verify {domain}".format(
                aiodnsbrute_program=aiodnsbrute_program,
                brute_dict=subdomain_dict_file,
                dns_server_list=dns_server_filename,
                output_file=subdomain_brute_output_filename,
                domain=self.domain
            )
            print(aiodnsbrute_work_cmd)
            aiodnsbrute_process_list.append({subprocess.Popen(
                aiodnsbrute_work_cmd, shell=True, stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL): subdomain_brute_output_filename})
        while aiodnsbrute_process_list[:]:
            # print(len(brute_process_list))
            time.sleep(1)
            for item in aiodnsbrute_process_list:
                for k, v in item.items():
                    # print(k.poll())
                    if k.poll() is None:
                        continue
                    elif k.poll() == 0:
                        aiodnsbrute_process_list.remove(item)
                        with open(v, "r", encoding="utf-8") as f:
                            aiodnsbrute_result_list.extend(f)
        shutil.rmtree(self.aiodnsbrute_temp_path)
        # ['[{"domain": "m.baidu.com", "ip": ["220.181.38.129", "220.181.38.130"]}, {"domain": "vpn.baidu.com", "ip": ["220.181.50.162", "220.181.50.247", "220.181.3.195", "220.181.3.196", "220.181.50.248", "220.181.3.194"]}, {"domain": "mail.baidu.com", "ip": ["220.181.3.87"]}, {"domain": "www.baidu.com", "ip": ["220.181.38.150", "220.181.38.149"]}, {"domain": "ns1.baidu.com", "ip": ["110.242.68.134"]}, {"domain": "ns2.baidu.com", "ip": ["220.181.33.31"]}]']
        return aiodnsbrute_result_list

    def wildcard_lookup(self):
        """
        泛解析
        :return:
        """
        pass

    def api_lookup(self):
        """
        通过api接口
        :return:
        """
        pass

    def run(self):
        pass


def main(target):
    """
    :return:
    """
    w = Wkuma(domain=target)
    w.run()


if __name__ == '__main__':
    main("baidu.com")
