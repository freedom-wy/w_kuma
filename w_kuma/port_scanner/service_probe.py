import nmap
import json


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


if __name__ == '__main__':
    test_data = [{'ip': '103.234.72.46', 'ports': [{'port': 3306, 'proto': 'tcp', 'status': 'open'}, {'port': 80, 'proto': 'tcp', 'status': 'open'}, {'port': 21, 'proto': 'tcp', 'status': 'open'}, {'port': 443, 'proto': 'tcp', 'status': 'open'}, {'port': 8888, 'proto': 'tcp', 'status': 'open'}, {'port': 22, 'proto': 'tcp', 'status': 'open'}, {'port': 888, 'proto': 'tcp', 'status': 'open'}]}, {'ip': '103.234.72.50', 'ports': [{'port': 22, 'proto': 'tcp', 'status': 'open'}]}, {'ip': '103.234.72.49', 'ports': [{'port': 3306, 'proto': 'tcp', 'status': 'open'}, {'port': 8888, 'proto': 'tcp', 'status': 'open'}, {'port': 7000, 'proto': 'tcp', 'status': 'open'}, {'port': 888, 'proto': 'tcp', 'status': 'open'}, {'port': 80, 'proto': 'tcp', 'status': 'open'}, {'port': 22, 'proto': 'tcp', 'status': 'open'}, {'port': 443, 'proto': 'tcp', 'status': 'open'}, {'port': 21, 'proto': 'tcp', 'status': 'open'}, {'port': 7001, 'proto': 'tcp', 'status': 'open'}]}, {'ip': '103.234.72.43', 'ports': [{'port': 23443, 'proto': 'tcp', 'status': 'open'}, {'port': 22, 'proto': 'tcp', 'status': 'open'}, {'port': 80, 'proto': 'tcp', 'status': 'open'}, {'port': 23306, 'proto': 'tcp', 'status': 'open'}]}, {'ip': '103.234.72.47', 'ports': [{'port': 50050, 'proto': 'tcp', 'status': 'open'}, {'port': 8012, 'proto': 'tcp', 'status': 'open'}, {'port': 1999, 'proto': 'tcp', 'status': 'open'}, {'port': 809, 'proto': 'tcp', 'status': 'open'}, {'port': 80, 'proto': 'tcp', 'status': 'open'}, {'port': 54321, 'proto': 'tcp', 'status': 'open'}, {'port': 808, 'proto': 'tcp', 'status': 'open'}, {'port': 1443, 'proto': 'tcp', 'status': 'open'}, {'port': 4400, 'proto': 'tcp', 'status': 'open'}, {'port': 4431, 'proto': 'tcp', 'status': 'open'}, {'port': 4433, 'proto': 'tcp', 'status': 'open'}, {'port': 8033, 'proto': 'tcp', 'status': 'open'}, {'port': 22, 'proto': 'tcp', 'status': 'open'}]}, {'ip': '103.234.72.48', 'ports': [{'port': 443, 'proto': 'tcp', 'status': 'open'}, {'port': 80, 'proto': 'tcp', 'status': 'open'}, {'port': 7723, 'proto': 'tcp', 'status': 'open'}, {'port': 888, 'proto': 'tcp', 'status': 'open'}, {'port': 7253, 'proto': 'tcp', 'status': 'open'}, {'port': 49154, 'proto': 'tcp', 'status': 'open'}]}]
    for item in test_data:
        print(item)
        # s = ServiceProbe(ipinfo=item.get("ip"), portinfo=[str(port.get("port")) for port in item.get("ports")])
        # s.service_probe()
        break
