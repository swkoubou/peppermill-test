# peppermill-heatupAPI
peppermill heatupAPI

## 動作環境
python2.7.x

## 使い方
以下を端末で実行します
```bash
$ pip install -r requirements.txt # 必要パッケージのインストール
$ python heatup.py								# サーバ起動
```
[http://localhost:5000/analyze](http://localhost:5000/analyze) に適当にPOSTを送信するとJSON形式でTrueかFalseをランダムで返します。
