import flask
from flask import request, jsonify
import pandas as pd
import numpy as np
import pickle
import json
import sklearn
from sklearn.preprocessing import MinMaxScaler

def split_data(content):
    split_tempo = content.split(",")
    new_split = []
    
    for i in range(len(split_tempo)):
        new_split_temp = split_tempo[i].split(':')
        new_split.append(new_split_temp[1])
    return new_split


def return_string(number):
    list_weight = ["null", "insufficient weight", "normal weight", "overweight level I", "overweight level II", "obesity level I", "obesity level II", "obesity level III"]
    return list_weight[number]


model = pickle.load(open('rfr_model', 'rb'))

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.


ObesityData = pd.read_csv("Datasets/ObesityDataSet_raw_and_data_sinthetic.csv",sep=",")

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Application used for Pandas database</h1>
<p>A prototype API for finding out, based on previous data, the obesity level of someone</p>'''



@app.route('/api/predict', methods=['POST'])
def predict():
 
    if request.method == 'POST':
     
        content = request.data
        data_set = []

        data_set = split_data(str(content).strip("b").strip("'{").strip("}'"))
        new_string = ""
        for j in data_set:
            new_string = new_string + j + "_"
        new_string  = new_string[:-1]
        list_param = new_string.split("_")
        new_data = []
        for st in list_param:
            new_data.append(float(st))

        new_test = np.array(new_data)

        new_test = new_test.reshape(1,-1)

        prediction = model.predict(new_test)


        return return_string(int(round(prediction[0],0)))
        
        

@app.route('/api/v1/resources/head', methods=['GET'])
def api_all():

    return ObesityData.head(5).to_html()




app.run()