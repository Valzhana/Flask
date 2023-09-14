import asyncio
import aiohttp
import time
import argparse
import os

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


async def save_image(url):
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        async with session.get(url) as response:
            cont = await response.read()
            filename = f'{url.split("/")[-1]}'
            with open(f'images/{filename}', 'wb') as f:
                f.write(cont)
                print(f'{filename} downloaded in {(time.time() - start_time):.2f} seconds')


async def main():
    tasks = []
    parser = argparse.ArgumentParser()
    parser.add_argument('url_list', nargs="*")
    parser.parse_args()
    for url in URLS:
        tasks.append(asyncio.create_task(save_image(url)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print(f'Final time: {(time.time() - start_func_time):.2f} seconds')
