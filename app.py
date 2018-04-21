#!flask/bin/python
import simplejson as json
from flask import Flask
from flask import jsonify
from os import system
import label_image

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'brand': 'Opel',
        'model': 'Corsa A',
        'Conselho': 'foge'
    }
]

@app.route('/')
def index():
    return "Hell, World!"

@app.route('/recognize', methods=['GET'])
def recognize_car():
    return jsonify((label_image.call_comparation_function("/Users/jorgearaujo/Downloads/teste_mt07.jpg")))


if __name__ == '__main__':
    app.run(debug=True)
