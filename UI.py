from datetime import datetime
from flask import Flask, render_template, request, redirect
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
#db = SQLAlchemy(app)

#データベースの定義
'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True) #主キー
    title = db.Column(db.String(30), nullable = False) #titleは30文字以下という制限, 空はだめだよ
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable = False)
'''
#with app.app_context():
#   db.create_all()


@app.route('/', methods = ['GET', 'POST'])#GET, POSTが使えるようになる
def index():
    if request.method == 'GET':
        posts =  Post.query.order_by(Post.due).all() #期限順にソート
        return render_template('index.html', posts = posts)
    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')

        due = datetime.strptime(due , '%Y-%m-%d')
        new_post = Post(title = title, detail = detail, due = due)

        db.session.add(new_post)
        db.session.commit() #データベースに反映

        return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/detail/<int:id>') #idに属する詳細を表示
def read(id):
    post = Post.query.get(id) #IDに該当するデータをを取得
    return render_template('detail.html', post = post)

@app.route('/update/<int:id>', methods = ['GET', 'POST']) #idに属する詳細を表示
def update(id):
    post = Post.query.get(id) #IDに該当するデータをを取得
    if request.method == 'GET':
        #updateのページ
        return render_template('update.html', post = post)
    else:
        #データベースに反映
        #トップページに
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id>') #idに属する詳細を表示
def delete(id):
    post = Post.query.get(id) #IDに該当するデータをを取得

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

