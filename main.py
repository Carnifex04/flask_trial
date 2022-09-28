from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "My Name is Hriday Gupta!"


@app.route('/username/<name>')
def greet(name):
    return f"Hi {name}!"


if __name__ == '__main__':
    app.run(debug=True)
