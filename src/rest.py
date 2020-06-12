#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:03:54 2020

@author: ehens86
"""

from client import robin_stock_client
from config import CONFIG

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/rh/api/v0/price/instrument/<symbol>', methods=['GET'])
def get_tasks(symbol):
    resp = rh.get_historicals(symbol)
    return Response(json.dumps(resp), status=201, mimetype='application/json')


if __name__ == '__main__':
    rh = robin_stock_client()
    rh.login()
    app.run(debug=True, port = CONFIG['flask']['PORT'], host='0.0.0.0')