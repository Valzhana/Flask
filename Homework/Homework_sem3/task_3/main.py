# Задание №3
# 📌 Доработаем задачу про студентов
# 📌 Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# 📌 База данных должна содержать две таблицы: "Студенты" и "Оценки".
# 📌 В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# 📌 В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# 📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
# 📌 Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.
import random

from flask import Flask, render_template
from models import db, Student, Mark

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marks_students.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-student')
def add_students():
    for student in range(1, 10):
        new_student = Student(
            first_name=f'name{student}',
            last_name=f'surname{student}',
            email=f'{student}@mail.ru',
            group=random.randint(1, 5)
        )
        db.session.add(new_student)
    db.session.commit()
    print('Students added')

    for grade in range(1, 10):
        new_grade = Mark(
            subject=f'subject{grade}',
            mark=random.randint(1, 10),
            student_id=random.randint(1, 10))
        db.session.add(new_grade)
    db.session.commit()
    print('Marks added!')


@app.route('/students/')
def all_students():
    students = Student.query.all()
    marks = Mark.query.all()
    context = {'title': 'Students', 'students': students, 'marks': marks}
    return render_template('students.html', **context)
