# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# Load the model
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def helloIndex():
    return 'Hello World from Python Flask!'


@app.route('/api/', methods=['POST', 'GET', 'DELETE'])
@cross_origin()
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    krediMiktari = data["krediMiktari"]
    yas = data["yas"]
    evDurumu = data["evDurumu"]
    aldigi_kredi_sayi = data["aldigi_kredi_sayi"]
    telefonDurumu = data["telefonDurumu"]

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[krediMiktari, yas, evDurumu, aldigi_kredi_sayi, telefonDurumu]])

    # Take the first value of prediction

    return jsonify(int(prediction[0]))


if __name__ == '__main__':
    app.run(port=5000)
