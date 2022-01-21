import subprocess


def test():
    process_list = [{subprocess.Popen(["python", "test.py"], stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL): "进程号{}".format(i)} for i in range(1, 4)]
    while process_list[:]:
        for item in process_list:
            for k, v in item.items():
                process_return = k.poll()
                if process_return is None:
                    print("{}正在运行".format(v))
                elif process_return == 0:
                    print("{}运行结束".format(v))
                    process_list.remove(item)
                elif process_return == 1:
                    print("{}sleep状态".format(v))
                elif process_return == 2:
                    print("{}进程不存在".format(v))
                elif process_return < 0:
                    print("{}进程已被杀死".format(v))


test()
