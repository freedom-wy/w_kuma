import subprocess

# check用于捕获异常
# process = subprocess.run("exit 1", shell=True, check=True)
# capture_output用于捕获stdout和stderr
# process = subprocess.run("ls -l", shell=True, check=True, capture_output=True)
# print(process.stdout.decode())
# 当子进程运行超时时可以通过subprocess.TimeoutExpired捕获,捕获后可以通过.stdout查看超时前输出
# try:
#     process = subprocess.run("python test.py".split(), capture_output=True, timeout=2)
# except subprocess.TimeoutExpired as e:
#     # print(e.output.decode())
#     print(e.stdout.decode())
# 子进程异常可通过subprocess.CalledProcessError捕获
# try:
#     process = subprocess.run("exit 1", shell=True, check=True)
# except subprocess.CalledProcessError as e:
#     print(e.stderr)
# 更高级的subprocess,使用subprocess.Popen
# process = subprocess.Popen(args="python test.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # 查看进程是否结束,如果正在运行返回None,否则返回returncode
# print(process.poll())
# print(process.stdout.read().decode())
# process = subprocess.Popen(args="python test.py", shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE
#                                )
# print(process.poll())
# process.kill()
# process.terminate()
p = subprocess.Popen('xargs ls', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
outs, errs = p.communicate(input='/Users/niulanshan'.encode())
# print(p.args)
print(outs.decode())
