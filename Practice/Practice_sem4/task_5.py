# Задание №5
# 🐀 Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# 🐀 Используйте процессы.

import multiprocessing
import time
import os

PATH = 'parser_url'
counter = multiprocessing.Value('i', 0)


def count_words(counter, filename) -> None:
    with open(filename, encoding='utf-8') as f:
        with counter.get_lock():
            counter.value += len(f.read().split())
    print(f'Значение счетчика: {counter.value:_}')


if __name__ == '__main__':
    processes = []
    start_time = time.time()

    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            process = multiprocessing.Process(target=count_words, args=(counter, file_path))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

    print(f'Amount of words is: {counter.value}')