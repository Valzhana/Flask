from flask import Flask, request, make_response, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'db025b60d89e84e5d6e476e02a0dc1293df14a62ac57f22ec64ac8c2d397304d'


@app.route('/')
def index():
    if 'username' in session:
        return f'Привет, {session["username"]}'
    else:
        redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
