# Задание №7
# 📌 Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# 📌 Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# 📌 Данные о новостях должны быть переданы в шаблон через
# контекст.
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/news/')
def news():

    news_block = [
        {
            'title': 'Фестиваль вина',
            'description': 'новости культуры',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'Инвестиции сегодня',
            'description': 'новости бизнесса',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года'),
        },
        {
            'title': 'Модный дом в Италии',
            'description': 'новости моды',
            'created_at': datetime.now().strftime('%H:%M - %m.%d.%Y года')
        }
    ]
    return render_template('news.html', news_block=news_block)


if __name__ == '__main__':
    app.run(debug=True)