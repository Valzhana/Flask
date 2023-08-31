# Задание №4
# Написать функцию, которая будет принимать на вход строку выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/string/<string:name>')
def text(name: str):
    return str(len(name))


if __name__ == '__main__':
    app.run(debug=True)