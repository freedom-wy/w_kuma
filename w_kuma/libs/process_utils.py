from enum import Enum


class ProcessStatusEnum(Enum):
    # 运行中
    Running = None
    # 正常退出
    End = 0


class ProcessStatus(object):
    def __init__(self, status):
        self._status = status

    @property
    def status(self):
        return ProcessStatusEnum(self._status)

    @status.setter
    def status(self, process_status):
        self._status = process_status.value

