#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""
heatup API

USAGE:
Run the following command in your terminal.
$ python heatup.py
"""
import os
import json
import burstditector

from flask import Flask, request, redirect, url_for, abort
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './tmp' # Path to the uploads
ALLOWED_EXTENSIONS = set(['wav'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """
    許可されたファイルか否かを判定する
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/analyze', methods=['POST'])
def analyze():
    # リクエストにfileあるか調べる
    if len(request.files) < 1:
        abort(400)

    wavefile = request.files[request.files.keys()[0]]   # ファイルを取り出す
    # もしユーザがファイルを選択していなかった場合,
    # ブラウザはfilenameに空の文字列を指定する.
    if wavefile.filename == '':
        abort(400)

    if wavefile and allowed_file(wavefile.filename):
        # アップロードされたファイルの保存
        filename = secure_filename(wavefile.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        wavefile.save(filepath)

        # burst ditectorの実行
        bd = burstditector.BurstDitector()
        response = {}
        if bd.is_burst(filepath):
            response['is_burst'] = True
        else:
            response['is_burst'] = False
        return json.dumps(response)


if __name__ == '__main__':
    app.run()
