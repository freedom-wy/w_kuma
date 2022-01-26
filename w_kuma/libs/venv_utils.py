import sys
import os


def is_venv():
    """
    判断当前环境是否为虚拟环境
    :return:
    """
    return hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)


def __check_root():
    return os.getuid() == 0


def __check_target(target: str):
    return target.strip() != "127.0.0.1"


def check_operate_env(target: str):
    """
    检查运行环境
    判断当前执行权限是否为root权限
    判断扫描目标是否为127.0.0.1
    :return:
    """
    if __check_root() and __check_target(target):
        return True
