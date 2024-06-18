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
