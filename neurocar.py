from flask import Flask
from flask import jsonify, request
from os import system
import label_image
from flask_cors import CORS
import requests
from io import open as iopen
from urlparse import urlsplit
import urllib as urllib
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hell, World!"

@app.route('/recognize', methods=['POST'])
def recognize_car():
    data = request.data
    dataDict = json.loads(data)
    print(dataDict["url"])
    url = dataDict["url"]
    img_name = "image.jpg"
    f = open(img_name,'wb')
    f.write(urllib.urlopen(url).read())
    f.close()
    return jsonify((label_image.call_comparation_function(img_name)))


if __name__ == '__main__':
    app.run(debug=True)
