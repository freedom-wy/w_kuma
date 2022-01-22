import sys


def is_venv():
    """
    判断当前环境是否为虚拟环境
    :return:
    """
    return hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
