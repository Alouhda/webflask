from flask import Flask
from flask import request
import json


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
    

@app.route('/', methods=["POST"])
def req():
    data = request.form.to_dict(flat=False)
    with open('saved_data', 'a', encoding='utf-8') as file:
        json.dump(data['lst'], file)
        file.write('\n')
    return data
    

