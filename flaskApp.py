from flask import Flask,redirect,url_for,render_template,request
from flask.helpers import make_response
from flask import jsonify
import methods as methods
import json
import random

#make sure ur cmd prompt is in the correct folder
#set FLASK_APP=main.py
#set FLASK_DEBUG=1
#flask run

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def main():
    return render_template('writeText.html')

@app.route('/data', methods=["POST","GET"])
def data():
    if request.method == 'GET':
        path = 'data.json'
        with open(path, 'r') as f:
            data = json.load(f)
        print(data)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        print(data)
        return jsonify(data)
    
