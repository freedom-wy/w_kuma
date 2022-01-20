import math
from config import *
import sys
import os
import subprocess
from multiprocessing import cpu_count


class Wkuma(object):
    def __init__(self, domain):
        self.enable_brute = True
        self.result = {}
        self.domain = domain
        self.subdomain_dict_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), subdomain_dict_path)
        self.subdomain_dict_file_list = self.split_subdomain_dict_file()

    def split_subdomain_dict_file(self):
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
        # 1、查找aiodnsbrute路径
        aiodnsbrute_path = self.aiodnsbrute_path()
        if not aiodnsbrute_path:
            raise ModuleNotFoundError("aiodnsbrute包未安装")
        aiodnsbrute_program = "LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 {python_interpreter} {aiodnsbrute_program}".format(
            python_interpreter=sys.executable, aiodnsbrute_program=aiodnsbrute_path)
        # 处理子域名文件
        # aiodnsbrute执行命令
        for subdomain_dict_file in self.subdomain_dict_file_list:
            aiodnsbrute_work_cmd = "{aiodnsbrute_program} -w {brute_dict} -r {dns_server_list} -f {output_file} -o json -t 5000 --no-verify {domain}".format(
                aiodnsbrute_program=aiodnsbrute_program,
                brute_dict=subdomain_dict_file,
                dns_server_list=dns_server_filename,
                output_file="aiodnsbrute_result.json",
                domain=self.domain
            )
            # pass
            # subprocess.Popen(aiodnsbrute_work_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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


def main():
    """
    :return:
    """
    w = Wkuma(domain="baidu.com")
    w.subdomain_brute()


if __name__ == '__main__':
    main()
