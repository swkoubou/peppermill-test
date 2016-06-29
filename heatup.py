#!/usr/bin/env python
"""
heatup API

USAGE:
Run the following command in your terminal.
$ exprot FLASK_APP=heatup.py
$ flask run
"""
from flask import Flask, request
import json

from random import randrange
app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    response = {}
    if randrange(1, 3) == 1:
        response['is_burst'] = True
    else:
        response['is_burst'] = False
    return json.dumps(response)

if __name__ == '__main__':
    app.run()
