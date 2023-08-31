# Задание №3
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<int:num_1>/<int:num_2>')
def sum_nums(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


if __name__ == '__main__':
    app.run(debug=True)
