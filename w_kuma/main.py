from config import *
import sys


class Wkuma(object):
    def __init__(self):
        self.dns_server = dns_server_list
        self.enable_brute = True
        self.result = {}

    def check_aiodnsbrute(self):
        aiodnsbrute_path = None
        if self.is_venv():
            aiodnsbrute_path = None
        else:
            aiodnsbrute_path = None

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
        pass

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


def main():
    """
    使用多线程处理
    :return:
    """
    pass


if __name__ == '__main__':
    main()
