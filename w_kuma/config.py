"""
配置文件
"""


# 子域名探测
# 是否开启子域名爆破
enable_brute = True
# 子域名字典
subdomain_filename = "subnames_full.txt"
# top子域名字典
top_subdomain_filename = "subnames_sub.txt"
# 子域名字典开关,FULL或SUB
subdomain_flag = "SUB"
# 子域名字典文件目录名称
subdomain_dict_path = "domain_resource"
# DNS server列表
dns_server_list = [
    "119.29.29.29", "182.254.116.116", "180.76.76.76", "223.5.5.5", "223.6.6.6",
    "114.114.114.114", "114.114.115.115", "8.8.8.8", "8.8.4.4"
]
# zoomeye api接口
zoomeye_api = "https://api.zoomeye.org/domain/search?q={}&type=1&page={}"

# 端口扫描
# masscan每次扫描IP数量
masscan_scan_size = 500
# masscan扫描速率
masscan_scan_rate = 10000
# masscan可执行程序路径,绝对路径/xxx/xxx/masscan
masscan_bin = ""
