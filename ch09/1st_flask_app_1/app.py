# -*- encoding: utf-8 -*-

from flask import Flask, render_template

# Flaskインスタンスを__name__(実行モジュール名)で初期化
app = Flask(__name__)

# ルーティング
@app.route('/')
# /に対応する関数を実装…連プレートを読み込んでいるだけ
def index():
    return render_template('first_app.html')

# pythonインタプリタで直接実行された時(__main__)の時、runを実行
if __name__ == '__main__':
    app.run()
