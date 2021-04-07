import requests
import random
from create_random_lst import ls_for
import time

#res = requests.get("http://127.0.0.1:5000/")

#print(res)
while True:
    print("Send reques")
    res = requests.post("http://127.0.0.1:5000/", {"lst": ls_for()})
    time.sleep(3)
