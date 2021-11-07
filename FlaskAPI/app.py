import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in # since we have a lot of data coming in
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.pkl"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    # stub input features 
    request_json = request.get_json()
    x = request_json['input'] # pass a list
    #print(x)
    x_in = np.array(x).reshape(1,-1) # send the x_in array to client
    # load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)