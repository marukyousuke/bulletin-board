# 掲示板プロジェクト/
# app.py           # Flaskアプリケーションのメインファイル
# templates/
#  index.html   # 投稿一覧の表示用HTMLテンプレート
#  create.html  # 新規投稿作成用HTMLテンプレート
# static/
# style.css    # スタイルシート

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 投稿データを格納するためのリスト
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        content = request.form['message']
        if content:
            posts.append({'msg': content})
            return redirect(url_for('create'))
    return render_template('create.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)



