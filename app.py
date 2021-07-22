from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Blog post {self.id}'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = BlogPost(
            title=post_title,
            content=post_title,
            author='dunfred',
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')

    all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
    return render_template('posts.html', posts=all_posts)


@app.route('/home/<string:name>', methods=['GET'])
def hello(name):
    return f'Hello {name}'


@app.route('/onlyget', methods=['GET'])
def get_only():
    return 'You can only get this webpage'
    

if __name__ == '__main__':
    app.run(debug=True)