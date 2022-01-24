import subprocess

process = subprocess.Popen(["python", "test.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
while True:
    process_return = process.poll()
    print(process_return)
