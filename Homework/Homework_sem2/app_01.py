# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя,
# а также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, request, make_response, render_template, redirect

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    name = request.form['name']
    email = request.form['email']
    response = make_response(redirect('/greeting'))
    response.set_cookie('user_name', name)
    response.set_cookie('user_email', email)
    return response


@app.route('/greeting')
def greeting():
    user_name = request.cookies.get('user_name')
    if user_name:
        return render_template('greeting.html', name=user_name)
    return redirect('/')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('user_name')
    response.delete_cookie('user_email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
