from flask import Flask, request, jsonify
from betting_ai_project import model, main
from betting_ai_project.model import *
from webscraping.matchesScraper.matchesScraper.spiders import ligaspider
from webscraping.matchesScraper.matchesScraper import middlewares

from icecream import ic
from bs4 import BeautifulSoup

import requests
import json
import re


app = Flask(import_name="subJavaFlaskApplication")
url = "https://1xlite-769674.top/ru/live/football/"


scrapped_data = {}
i = len(scrapped_data)
result_data = {}

xgb_predictor = model.MatchPredictor(model = xgb_model)
rf_predictor = model.MatchPredictor(model = rf_model)

@app.route('/scrap_data/<id>', methods=['GET'])
def scrap_data(id):
    # scrap data from webscrapping submodule'
    id_url = url + id
    response = requests.get(url = id_url)
    if (response.status_code != 200):
        return requests.post("http::/localhost:8080/error", data=404)
    soup = BeautifulSoup(response.text, 'lxml')




@app.route('/make_prediction/<string:id>', methods = ['GET'])
def make_prediction(id):
    # make prediction using betting_ai_project submodule

    if not id in scrapped_data:
        scrapped_data[id] = scrap_data(id)

    result_data = xgb_predictor.predict_and_recommend(scrapped_data[id])

    with open("data.json", "w") as json_file:
        json.dump(json_file,  result_data)

    int_numbers = re.findall(r'\b\d+\b', id)

    int_id = int_numbers[0]

    response = requests.post(f'http://localhost:8080/prediction/{int_id}', json=json_file)

    if response.status_code == 200:
        ic("Prediction was sent to Spring")
    else:
        ic("Failed to send the prediction")