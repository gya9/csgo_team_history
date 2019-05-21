from flask import Blueprint, jsonify, request, render_template
from random import *
import pandas as pd
import numpy as np

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@api.route('/df/teamlist')
def team_list():
    df = pd.read_csv('backend/team_history.csv', index_col=0, parse_dates=True)
    

@api.route('/df/<string:search_word>')
def df_data(search_word):
    import datetime as dt
    df = pd.read_csv('backend/team_history.csv', index_col=0, parse_dates=True)
    tmp = []
    response = {}

    for date in df.index:
        tmp2 = list(df.columns[df.loc[date] == search_word.replace(' ','_')])
        if tmp2 != tmp and len(tmp2) == 5:
            tmp = tmp2

            response[date.strftime('%Y-%m-%d')] = tmp

    return jsonify(response)