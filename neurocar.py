from flask import Flask
from flask import jsonify
from os import system
import label_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hell, World!"

@app.route('/recognize', methods=['POST'])
def recognize_car():
    return jsonify((label_image.call_comparation_function("teste_mt07.jpg")))


if __name__ == '__main__':
    app.run(debug=True)
