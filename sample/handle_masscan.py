ip_list = ["127.0.0.{}".format(i) for i in range(1, 255)]
combine_ip_set = ip_list
batch_size = 20
win_num = int(len(combine_ip_set) / batch_size) + (1 if len(combine_ip_set) % batch_size else 0)
print(win_num)
for i in range(win_num):
    win_start, win_stop = i * batch_size, min((i+1)*batch_size, len(combine_ip_set))
    cmd = "masscan {ip} -p{port_range} --rate={rate} -oX {xml_path}".format(
        ip=",".join(combine_ip_set[win_start:win_stop]),
        port_range="1-65535", rate="10000", xml_path="test.xml")
    print(cmd)


