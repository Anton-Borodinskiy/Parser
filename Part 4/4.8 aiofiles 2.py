#IMAGES
import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def write_file(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


async def main():
    url = 'https://parsinger.ru/asyncio/aiofile/1/index.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            img_url = [f'https://parsinger.ru/asyncio/aiofile/1/{x["src"]}' for x in soup.find_all('img')]
            tasks = []
            for link in img_url:
                name_img = link.split('/')[7]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')



#VIDEO SYNC AND ASYNC
import requests
import time
import aiofiles
import asyncio
import aiohttp

url = 'https://parsinger.ru/asyncio/aiofile/1/video/nu_pogodi.mp4'


def sync_write():
    with open('video/sync_video_async.mp4', 'wb') as video:
        response = requests.get(url, stream=True)
        for piece in response.iter_content(chunk_size=5120):
            video.write(piece)


async def async_write():
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('video/async_video_async.mp4', mode='wb') as video:
            async with session.get(url) as response:
                async for piece in response.content.iter_chunked(5120):
                    await video.write(piece)


start = time.perf_counter()
sync_write()
print(f'Cохранено синхронным способом за {round(time.perf_counter() - start, 3)} сек')

start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(async_write())
print(f'Cохранено асинхронным способом за {round(time.perf_counter() - start, 3)} сек')



#SYNC AND ASYNC
import os
import time
import aiofiles
import asyncio

path = os.listdir('file_text')


def sync_mass_read(path):
    start = time.perf_counter()
    for file in path:
        with open(f"file_text/{file}", 'r') as f:
            for line in f:
                print(line.strip())
    sync_time = round(time.perf_counter() - start, 5)
    return sync_time


async def async_mass_read(path):
    start = time.perf_counter()
    for file in path:
        async with aiofiles.open(f'file_text/{file}', mode='r') as f:
            async for line in f:
                print(str(line).strip())
        async_time = round(time.perf_counter() - start, 5)
        return print(f"Файл считан построчно в асинхронном стиле за {async_time} сек")


sync = sync_mass_read(path)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(async_mass_read(path))
print(f"Файл считан построчно в синхронном стиле за {sync} сек")



