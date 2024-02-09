import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
#TASK2
async def write_file(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


async def main():
    url = 'https://parsinger.ru/asyncio/aiofile/3/index.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            all_urls_L1 = [f'https://parsinger.ru/asyncio/aiofile/3/{x["href"]}' for x in soup.find_all('a', href=True)]
            all_urls_L2 = []
            for url2 in all_urls_L1:
                async with aiohttp.ClientSession() as session2:
                    async with session2.get(url2) as response2:
                        soup2 = BeautifulSoup(await response2.text(), 'lxml')
                        img_url = [f'{url2.split("category")[0]}{x["href"]}' for x in soup2.find_all('a', href=True)]
                        all_urls_L2.extend(img_url)
            all_imgs = []
            for url2 in all_urls_L2:
                async with aiohttp.ClientSession() as session2:
                    async with session2.get(url2) as response2:
                        soup2 = BeautifulSoup(await response2.text(), 'lxml')
                        print(url2)
                        img_url = [f'{x["src"]}' for x in soup2.find_all('img')]
                        all_imgs.extend(img_url)
            all_imgs = list(set(all_imgs))
            print(len(all_imgs))
            tasks = []
            for link in all_imgs:
                name_img = link.split('/')[-1]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')

def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
print(get_folder_size("images/"))

#EXAMPLE
import aiofiles
import asyncio
import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry
from bs4 import BeautifulSoup
import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import logging


class AsyncDeepImagesDowloader:
    def __init__(self, root):
        self.root = root
        self.total_size = 0
        self.level2_links = []
        self.images_links = set()

    def get_level1_links(self, url):
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        return map(lambda tag: self.root + tag['href'], soup.find_all('a'))

    def get_level2_links(self, url):
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        image_pages = [''.join((self.root, 'depth2/', x['href'])) for x in soup.find_all('a')]
        self.level2_links.extend(image_pages)

    async def download(self, session, url, pbar):
        async with aiofiles.open(f'images/{url.split("/")[6]}.jpg', 'wb') as fout:
            async with session.get(url) as response:
                pbar.update()
                async for chunck in response.content.iter_chunked(3072):
                    await fout.write(chunck)

    async def get_images(self, session, url, pbar):
        retry_options = ExponentialRetry(attempts=5)
        retry_client = RetryClient(retry_options=retry_options, client_session=session, start_timeout=0.5)

        async with retry_client.get(url) as page_response:
            if page_response.ok:
                p_response = await page_response.text()
                p_soup = BeautifulSoup(p_response, 'lxml')
                links = list(map(lambda x: x['src'], p_soup.find_all('img')))
                pbar.update()
                self.images_links.update(links)

    async def parse_site(self):
        async with aiohttp.ClientSession() as session:
            pbar = tqdm(total=len(self.level2_links), desc='Обработка ссылок 2 уровня : ', colour='WHITE')
            links_tasks = []
            for link in self.level2_links:
                link_task = asyncio.create_task(self.get_images(session, link, pbar))
                links_tasks.append(link_task)
            await asyncio.gather(*links_tasks)
            pbar.close()

            pbar = tqdm(total=len(self.images_links), desc='Скачивание изображений: ', colour='YELLOW')
            download_tasks = []
            for img in self.images_links:
                img_task = asyncio.create_task(self.download(session, img, pbar))
                download_tasks.append(img_task)
            await asyncio.gather(*download_tasks)
            pbar.close()

    def get_folder_size(self, filepath):
        for root, dirs, files in os.walk(filepath):
            for img in files:
                self.total_size += os.path.getsize(os.path.join(root, img))

    def __call__(self, main_page, *args, **kwargs):
        level1_links = self.get_level1_links(main_page)

        with ThreadPoolExecutor(30) as pool:
            pool.map(self.get_level2_links, tqdm(level1_links, desc='Обработка ссылок 1 уровня: ', total=100))

        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.parse_site())

        self.get_folder_size('images')
        print(f'Общий размер скачанных изображений: {self.total_size}')



if __name__ == '__main__':
    try:
        image_dowloader = AsyncDeepImagesDowloader(root='https://parsinger.ru/asyncio/aiofile/3/')
        image_dowloader(main_page='https://parsinger.ru/asyncio/aiofile/3/index.html')
    except Exception as error:
        logging.error(f'Парсер аварийно завершил работу: {error}')
#TASK1
async def write_file(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


async def main():
    url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            all_urls = [f'https://parsinger.ru/asyncio/aiofile/2/{x["href"]}' for x in soup.find_all('a', href=True)]
            all_imgs = []
            for url2 in all_urls:
                async with aiohttp.ClientSession() as session2:
                    async with session2.get(url2) as response2:
                        soup2 = BeautifulSoup(await response2.text(), 'lxml')
                        img_url = [f'{x["src"]}' for x in soup2.find_all('img')]
                        all_imgs.extend(img_url)
            print(all_imgs)
            tasks = []
            for link in all_imgs:
                name_img = link.split('/')[-1]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(f'Cохранено изображений {len(os.listdir("images/"))} за {round(time.perf_counter() - start, 3)} сек')

def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
print(get_folder_size("images/"))


#EXAMPLE
import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


async def write_file(session, url, name_img):
    async with aiofiles.open(f'F:\\img\\{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for file in response.content.iter_chunked(2048):
                await f.write(file)
        print(f'Изображение сохранено {name_img}')


async def main(url):
    schema = 'https://parsinger.ru/asyncio/aiofile/2/'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            all_page = [schema + x['href'] for x in soup.find_all('a')]
            all_url_image = []
            for x in all_page:
                async with session.get(x) as response2:
                    soup2 = BeautifulSoup(await response2.text(), 'lxml')
                    all_url_image.extend([x['src'] for x in soup2.find_all('img')])
            tasks = []
            for link in all_url_image:
                name_img = link.split('/')[6]
                task = asyncio.create_task(write_file(session, link, name_img))
                tasks.append(task)
            await asyncio.gather(*tasks)


path = 'zadacha1/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
url = 'https://parsinger.ru/asyncio/aiofile/2/index.html'
asyncio.run(main(url))

print(f'Cохранено {len(os.listdir(path))} изображений за {round(time.perf_counter() - start, 3)} сек')


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size
print(f'Размер всех изображений {get_folder_size(path)} byte')