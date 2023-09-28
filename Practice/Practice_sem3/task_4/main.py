# Задание №4
# 📌 Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна
# содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# 📌 После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее
# сообщение об ошибке.
# 📌 Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение
# об ошибке.

from flask import Flask, render_template, request
from flask_wtf import CSRFProtect

from models import db, Users
from forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_users.db'
db.init_app(app)


app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        user_name = form.user_name.data
        email = form.email.data
        password = form.password.data
        users = Users(user_name=user_name, email=email, password=password)
        db.session.add(users)
        db.session.commit()
        return f'Вы успешно зарегистрированы'
    return render_template('register.html', form=form)


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    users = Users.query.all()
    return f'{list(users)}'

