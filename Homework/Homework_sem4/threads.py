
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле,
# название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания
#   каждого изображения и общем времени выполнения программы.

import argparse
from threading import Thread
import time
import os
import requests

URLS = [
    'https://bigpicture.ru/wp-content/uploads/2019/03/3175212_-688x748.jpg',
    'https://bigpicture.ru/wp-content/uploads/2019/03/933e3b4086a11ce70cd9772e0ba0e2f2.jpg',
    'https://basetop.ru/wp-content/uploads/2016/12/2sp23jfu.jpg',
    'https://cdn.fishki.net/upload/post/201508/21/1636221/11.jpg',
    'https://pibig.info/uploads/posts/2022-02/1644780963_9-pibig-info-p-krasnie-ovoshchi-i-frukti-priroda-krasivo-16.jpg',
    'https://pibig.info/uploads/posts/2022-02/1644780898_18-pibig-info-p-krasnie-ovoshchi-i-frukti-priroda-krasivo-36.jpg',
    'https://static.kulturologia.ru/files/u18476/SofiLoren-14.jpg',
    'https://static.kulturologia.ru/files/u27045/270455430.jpg'
]

start_func_time = time.time()
if not os.path.exists('images'):
    os.makedirs('images')


def save_image(url):
    response = requests.get(url)
    filename = f'{url.split("/")[-1]}'
    with open(f'images/{filename}', 'wb') as f:
        f.write(response.content)
        print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


threads = []
start_time = time.time()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    args = parser.parse_args()
    return args.url_list


if __name__ == '__main__':
    for url in URLS:
        thread = Thread(target=save_image, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final time: {(time.time() - start_func_time):.2f} seconds')
