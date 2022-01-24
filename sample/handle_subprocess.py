# import subprocess
#
# process = subprocess.Popen(["python", "test.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# while True:
#     process_return = process.poll()
#     print(process_return)

from enum import Enum


class VIP(Enum):
    """
    定义一个类继承枚举类
    """
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4
    # RED = 5 报错，相同的常量
    # 枚举类特点1、不能修改枚举类中常量值，枚举类中常量值不能相同


print(VIP.YELLOW == 1)  # False
print(VIP.YELLOW == VIP(1))  # True

# print(VIP.YELLOW, type(VIP.YELLOW))
# print(VIP.YELLOW.name, type(VIP.YELLOW.name))
# print(VIP.YELLOW.value, type(VIP.YELLOW.value))
# VIP.YELLOW = 5 报错


# class VIP1(Enum):
#     YELLOW = 1
#     GREEN = 2
#     BLACK = 3
#     RED = 4


# print(VIP.YELLOW == VIP.GREEN)  # False
# print(VIP.GREEN == VIP.GREEN)  # True
# print(VIP.GREEN == VIP1.GREEN)  # False
