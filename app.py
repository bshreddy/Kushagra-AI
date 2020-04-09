from flask import Flask, request, jsonify
import base64

import crop_model
import disease_model

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome. This is a Flask AI Inference Server"

@app.route("/crop", methods=["POST"])
def crop():
    file = request.files["img"]
    img_bytes = file.read()
    return jsonify(crop_model.get_crop_prediction(img_bytes))

@app.route("/disease", methods=["POST"])
def disease():
    file = request.files["img"]
    img_bytes = file.read()
    return jsonify(disease_model.get_disease_prediction(img_bytes))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)