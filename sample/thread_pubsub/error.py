class NoChannelError(Exception):
    def __init__(self, error_info):
        self.error_info = error_info

    def __str__(self):
        return self.error_info


if __name__ == '__main__':
    try:
        raise NoChannelError("无订阅频道")
    except NoChannelError as e:
        print(e)
