import requests
import random
from create_random_lst import ls_for

res = requests.get("http://127.0.0.1:5000/")

print(res.text)
print(ls_for)
