import requests
import random
from create_random_lst import ls_for
import time

#res = requests.get("http://127.0.0.1:5000/")
# ^ закомментированный лучше удалять, что бы не мазолил глаз и не заставлял гадать, зачем он нужен


#print(res)
# ^ комментарии лучше удалять

while True:
    print("Send reques")
    res = requests.post("http://127.0.0.1:5000/", {"lst": ls_for()})
    #                   ^ лучше задасть в начале скрипта как константу
    time.sleep(3)
