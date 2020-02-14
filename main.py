from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def homepage():
    return 'This is our home page'


@app.route('/hello')
def hello():
    return 'THis is hello page'


@app.route('/<name>')
def other_page(name):
    return "hello " + name


if __name__ == '__main__':
    app.run(debug=True)


