# Задание №5
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/world/')
def world():
    return render_template('world.html')


if __name__ == '__main__':
    app.run(debug=True)