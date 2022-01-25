import sys
import os


def is_venv():
    """
    判断当前环境是否为虚拟环境
    :return:
    """
    return hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)


def check_root():
    """
    判断当前执行权限是否为root权限
    :return:
    """
    return os.getuid() == 0

