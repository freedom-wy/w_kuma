import os
import subprocess
import uuid
from multiprocessing import cpu_count
import math
from config import *
from w_kuma.libs.venv_utils import is_venv
import sys
from aiodnsbrute.cli import aioDNSBrute


class SingleSubDomainData(object):
    """
    规范输出
    """

    def __init__(self, subdomain_info):
        self.subdomain = subdomain_info.get("subdomain")
        self.ip = ",".join(subdomain_info.get("ip"))
        self.subdomain_flag = subdomain_info.get("subdomain_flag")


class CollectionSubDomainData(object):
    def __init__(self):
        self.total = 0
        self.subdomains = []
        self.domain = None

    def fill(self, subdomains, domain):
        self.total = len(subdomains.get("result"))
        self.subdomains = [SingleSubDomainData(subdomain_info) for subdomain_info in subdomains.get("result")]
        self.domain = domain


class DomainScan(object):
    def __init__(self, domain):
        self.result = {}
        self.domain = domain
        # 工作目录
        self.work_dir = os.path.dirname(os.path.abspath(__file__))
        # 子域名字典目录
        self.subdomain_dict_path = os.path.join(self.work_dir, subdomain_dict_path)
        # 分割字典文件
        self.subdomain_dict_file_list = self.__split_subdomain_dict_file()
        # 泛解析字典
        self.wildcard_dict_path = os.path.join(self.subdomain_dict_path, "wildcard.txt")

    @staticmethod
    def __aiodnsbrute_path():
        """
        输出aiodnsbrute程序路径
        :return:
        """
        if is_venv():
            aiodnsbrute_path = os.path.join(os.path.dirname(sys.executable), "aiodnsbrute")
        else:
            aiodnsbrute_path = "/usr/local/bin/aiodnsbrute"
        return aiodnsbrute_path

    def __split_subdomain_dict_file(self):
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

    def subdomain_brute(self):
        """
        子域名爆破
        :return:
        """
        aiodnsbrute_result_list = []
        for file in self.subdomain_dict_file_list:
            result = aioDNSBrute().run(wordlist=file, domain=self.domain, resolvers=dns_server_list, verify=False)
            aiodnsbrute_result_list.extend(result)
        return aiodnsbrute_result_list

    def subdomain_wildcard_lookup(self):
        """
        子域名泛解析
        :return:
        """
        wildcard_lookup_result_set = set()
        result = aioDNSBrute().run(wordlist=self.wildcard_dict_path, domain=self.domain, resolvers=dns_server_list, verify=False)
        print(result)



    def subdomain_api(self):
        """
        通过API接口获取
        :param domain:
        :return:
        """
        pass

    def run(self):
        pass


def main(domain):
    # result = DomainScan(domain=domain).subdomain_brute()
    result = DomainScan(domain=domain).subdomain_wildcard_lookup()
    print(result)


if __name__ == '__main__':
    main(domain="taobao.com")
