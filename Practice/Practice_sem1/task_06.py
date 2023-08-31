# Задание №6
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с таблицей, содержащей информацию о студентах.
# 📌 Таблица должна содержать следующие поля: "Имя",
# "Фамилия", "Возраст", "Средний балл".
# 📌 Данные о студентах должны быть переданы в шаблон через
# контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/students/')
def students():
    head = {
        'first_name': 'Имя',
        'last_name': 'Фамилия',
        'age': 'Возраст',
        'rating': 'Средний балл'
    }

    students_list = [
        {
            'first_name': 'Семён',
            'last_name': 'Иванов',
            'age': 45,
            'rating': 78,
        },
        {
            'first_name': 'Иван',
            'last_name': 'Петров',
            'age': 25,
            'rating': 88,
        },
        {
            'first_name': 'Илья',
            'last_name': 'Владимиров',
            'age': 30,
            'rating': 60,
        }
    ]
    return render_template('students.html', **head, students_list=students_list)


if __name__ == '__main__':
    app.run(debug=True)