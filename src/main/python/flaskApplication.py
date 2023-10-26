from flask import Flask, request, jsonify
from IA_Soccer_Prediction import predict
from webscraping.matchesScraper.matchesScraper.spiders import ligaspider
from webscraping.matchesScraper.matchesScraper import middlewares

from icecream import ic
from bs4 import BeautifulSoup

import pandas as pd

import requests
import json
import re
import sys

app = Flask(import_name="subJavaFlaskApplication")
# url = "https://1xlite-769674.top/ru/live/football/"
local_url = "htpp::/localhost:8080"

scrapped_data = {}
i = len(scrapped_data)
result_data = {}
selected_teams = {}

# @app.route('/scrap_data/<string:id>', methods=['GET'])
# def scrap_data(id):
#     id_url = url + id
#     response = requests.get(url=id_url)
#     if response.status_code != 200:
#         return requests.post("http::/localhost:8080/error", data=404)
#     soup = BeautifulSoup(response.text, 'lxml')
#
#     for x in soup.findAll("div", "team-scores__teams team-scores-teams"):
#         teams = x.findAllNext('span', 'caption__label')
#         ic(teams)
#         if len(teams) == 2:
#             selected_teams[id] = {
#                 'team': teams[0].text,
#                 'opponent': teams[1].text
#             }
#
#     if id not in selected_teams:
#         return jsonify({"error": "No team names found"}), 404
#
#     selected_data = selected_teams[id]
#     X_train_selected = [selected_data]
#     X_test_selected = [selected_data]
#
#     return jsonify({"X_train_selected": X_train_selected, "X_test_selected": X_test_selected})


# @app.route('/make_prediction/<string:id>', methods=['GET'])
# def make_prediction(id):
#     # make prediction using betting_ai_project submodule
#
#     if id not in scrapped_data:
#         scrapped_data[id] = scrap_data(id)
#
#     rf_predictor.train(scrapped_data[id]['X_train_selected'], y_train)
#     xgb_predictor.train(scrapped_data[id]['X_train_selected'], y_train)
#
#     # Predict and recommend
#     result_data[0] = rf_predictor.predict_and_recommend(scrapped_data[id]['X_test_selected'])
#     result_data[1] = xgb_predictor.predict_and_recommend(scrapped_data[id]['X_test_selected'])
#
#     with open("data.json", "w") as json_file:
#         json.dump(result_data, json_file)
#
#
#     response = requests.post(f'http://localhost:8080/prediction/{id}', json=json_file)
#
#     if response.status_code == 200:
#         ic("Prediction was sent to Spring")
#     else:
#         ic("Failed to send the prediction")


@app.route('/make_prediction', methods=['GET','POST'])
def make_prediction():
    try:
        response = request.get_json()
        print(response, file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(jsonify({"error": "Request to Java application failed: " + str(e)}), 500)

    dataFrame = pd.json_normalize(response)

    result = predict.map_predictions_to_results(
        make_prediction(
            model=predict.load_trained_model(),
            input_data=dataFrame)
    )
    print(result)


    switch = {
        "L (Away team win)" : -1,
        "D (Draw)": 0,
        "W (Home team win)": 1
    }

    int_res = switch.get(result[0], default="Something went wrong with result")
    response = requests.post(f'http://localhost:8080/prediction', data = str(int_res))

    return response


if __name__ == "__main__":
    app.run(debug = True)
