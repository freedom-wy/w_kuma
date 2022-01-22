from aiodnsbrute.cli import aioDNSBrute


result = aioDNSBrute().run(wordlist="wildcard.txt", domain="taobao.com", verify=False, wildcard=False)
# print(result)
import uuid
for i in range(5):
    print(uuid.uuid4())

