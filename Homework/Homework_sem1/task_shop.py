# Задание №9
# 📌 Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню,
# подвал), и дочерние шаблоны для страниц категорий
# товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка",
# используя базовый шаблон


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base_shop/')
def base():
    return render_template('base_shop.html')


@app.route('/main/')
def main():
    return render_template('main_shop.html')


@app.route('/footwear/')
def footwear():
    return render_template('footwear.html')


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')


if __name__ == '__main__':
    app.run(debug=True)
