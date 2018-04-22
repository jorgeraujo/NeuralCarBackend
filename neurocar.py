from flask import Flask
from flask import jsonify, request
from os import system
import label_image
from flask_cors import CORS
import requests
from io import open as iopen
import urllib as urllib
import json

app = Flask(__name__)
CORS(app)

brand_models={}
brand_models['hondansxna1'] = ("Honda","NSX")
brand_models['opelcorsab'] = ("Opel","Corsa")
brand_models['renaultclio iv'] = ("Renault","Clio IV")
brand_models['porsche911 997'] = ("Porsche","991 997")
brand_models['yamaha mt 07'] = ("Yamaha","MT-07")




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
    i = requests.get(url)
    with iopen(img_name, 'wb') as file:
        file.write(i.content)
    result = label_image.call_comparation_function(img_name)
    return jsonify({"brand":brand_models[result[0][0]][0],"model":brand_models[result[0][0]][1],"accuracy":result[0][1]})


if __name__ == '__main__':
    app.run(debug=True)
