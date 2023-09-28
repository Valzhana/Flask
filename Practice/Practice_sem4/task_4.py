# Задание №4
# 🐀 Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# 🐀 Используйте потоки.

import threading
import time
import os

PATH = 'parser_url'
count = 0


async def count_words(filename: str) -> None:
    global count
    with open(filename, encoding='utf-8') as f:
        count += len(f.read().split())


if __name__ == '__main__':
    threads = []
    start_time = time.time()

    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            thread = threading.Thread(target=count_words, args=(file_path,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    print(f'Amount of words is: {count}')
