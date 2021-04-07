from flask import Flask
from flask import request
import json


was_saved = 0
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    

@app.route('/', methods=["POST"])
def req():
    data = request.form.to_dict(flat=False)
    with open('saved_data_' + str(was_saved), 'w', encoding='utf-8') as file:
        json.dump(data['lst'], file)
        file.write('\n')
    was_saved += 1
    return data
    

