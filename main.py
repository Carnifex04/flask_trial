from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, **kwargs) + '</b>'

    return wrapper


def make_italics(function):
    def wrapper(*args, **kwargs):
        return '<i>' + function(*args, **kwargs) + '</i>'

    return wrapper


def make_underlined(function):
    def wrapper(*args, **kwargs):
        return '<u>' + function(*args, **kwargs) + '</u>'

    return wrapper


@app.route('/')
def hello_world():
    return "My Name is Hriday Gupta!"


@app.route('/username/<name>/<surname>')
@make_italics
@make_bold
@make_underlined
def greet(name, surname):
    return f"Hi {name} {surname}!"


if __name__ == '__main__':
    app.run(debug=True)
