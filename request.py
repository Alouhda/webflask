import requests
import random
from create_random_lst import get_rand_list
import time

url = 'http://127.0.0.1:5000/'
while True:
    print("Send reques")
    res = requests.post(url, {'lst': get_rand_list()})
    time.sleep(3)
