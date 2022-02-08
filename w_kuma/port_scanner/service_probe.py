import concurrent.futures

import nmap
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED


class ServiceProbe(object):
    def __init__(self, ipinfo, portinfo: list):
        self.nm = nmap.PortScanner()
        self.ipinfo = ipinfo
        self.portinfo = portinfo

    def service_probe(self):
        """
        探测服务信息
        :return:
        """
        ports = ",".join(self.portinfo)
        result = self.nm.scan(hosts=self.ipinfo, ports=ports)
        return result


class CollectionServiceProbe(object):
    """
    多线程处理服务识别
    """

    def __init__(self):
        self.datas = []

    def run(self, ip_ports_info):
        # 根据默认值创建线程池
        with ThreadPoolExecutor() as pool:
            # 提交线程处理
            future_list = [pool.submit(self.__services_probe, item) for item in ip_ports_info]
        # 设置线程返回,有数据完成即返回
        concurrent.futures.wait(future_list, return_when=FIRST_COMPLETED)
        # 获取线程返回数据
        for future in concurrent.futures.as_completed(future_list):
            print(future.result())

    @staticmethod
    def __services_probe(item):
        return ServiceProbe(ipinfo=item.get("ip"), portinfo=[
            str(port.get("port")) for port in item.get("ports")]).service_probe()

    def __format_result(self):
        """
        处理多线程结果数据
        :return:
        """
        pass


if __name__ == '__main__':
    import json

    test_data = [{'ip': '103.234.72.46', 'ports': [{'port': 3306, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 80, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 21, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 443, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 8888, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 22, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 888, 'proto': 'tcp', 'status': 'open'}]},
                 {'ip': '103.234.72.50', 'ports': [{'port': 22, 'proto': 'tcp', 'status': 'open'}]},
                 {'ip': '103.234.72.49', 'ports': [{'port': 3306, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 8888, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 7000, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 888, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 80, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 22, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 443, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 21, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 7001, 'proto': 'tcp', 'status': 'open'}]},
                 {'ip': '103.234.72.43', 'ports': [{'port': 23443, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 22, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 80, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 23306, 'proto': 'tcp', 'status': 'open'}]},
                 {'ip': '103.234.72.47', 'ports': [{'port': 50050, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 8012, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 1999, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 809, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 80, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 54321, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 808, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 1443, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 4400, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 4431, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 4433, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 8033, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 22, 'proto': 'tcp', 'status': 'open'}]},
                 {'ip': '103.234.72.48', 'ports': [{'port': 443, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 80, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 7723, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 888, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 7253, 'proto': 'tcp', 'status': 'open'},
                                                   {'port': 49154, 'proto': 'tcp', 'status': 'open'}]}]
    c = CollectionServiceProbe()
    c.run(ip_ports_info=test_data)
