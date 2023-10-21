from flask import Flask, request, jsonify
from betting_ai_project import model, main
from betting_ai_project.model import *
from webscraping.matchesScraper.matchesScraper.spiders import ligaspider
from webscraping.matchesScraper.matchesScraper import middlewares

app = Flask(import_name="subJavaFlaskApplication")

scrapped_data = {}
i = len(scrapped_data)
result_data = {}

xgb_predictor = model.MatchPredictor(model = xgb_model)
rf_predictor = model.MatchPredictor(model = rf_model)

@app.route('/scrap_data/<int:id>', methods=['GET'])
def scrap_data(id):
    # scrap data from webscrapping submodule'


    pass

@app.route('/make_prediction/<int:id>', methods = ['GET'])
def make_prediction(id):
    # make prediction using betting_ai_project submodule

    if not id in scrapped_data:
        scrapped_data[id] = scrap_data(id)

    result_data = xgb_predictor.predict_and_recommend(scrapped_data[id])

    return






    pass