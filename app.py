from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'description': 'Today is a sunny daty',
    },
    {
        'title': 'Post 2',
        'description': 'Hello cynthia',
    },
    {
        'title': 'Post 2',
        'description': 'Halleluyah',
    },
]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def post():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/<string:name>', methods=['GET'])
def hello(name):
    return f'Hello {name}'

@app.route('/onlyget', methods=['GET'])
def get_only():
    return 'You can only get this webpage'

if __name__ == '__main__':
    app.run(debug=True)