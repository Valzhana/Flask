# Задание №6
# 🐀 Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# 🐀 Используйте асинхронный подход.

import asyncio
import time
import os

PATH = 'parser_url'
count = 0


async def count_words(file_path):
    global count
    with open(file_path, encoding='utf-8') as f:
        count = len(f.read().split())
    print(f'Значение счетчика: {count:_}')


async def main():
    tasks = []
    for root, dirs, files in os.walk(PATH):
        for filename in files:
            file_path = os.path.join(root, filename)
            tasks.append(asyncio.create_task(count_words(file_path)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print({count})
    start_time = time.time()
    print(start_time)
