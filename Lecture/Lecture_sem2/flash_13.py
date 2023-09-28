from flask import Flask, request, make_response, render_template, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'db025b60d89e84e5d6e476e02a0dc1293df14a62ac57f22ec64ac8c2d397304d'

"""
Генерация надёжного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        if not request.form['name']:
            flash('Введите имя', 'danger')
            return redirect(url_for('form'))
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)