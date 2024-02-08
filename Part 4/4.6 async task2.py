import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
category_links = soup.find_all("a", class_="lnk_img")
schema = "https://parsinger.ru/asyncio/create_soup/1/"
codes = []
async def run_tasks(url, session):
    async with session.get(url) as resp:
        if resp.ok:
            soup2 = BeautifulSoup(await resp.text(), 'html.parser')
            if soup2.find("p", class_="text").text.isdigit():
                return int(soup2.find("p", class_="text").text)
            else:
                return 0
        else:
            return 0
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(f'{schema}{link["href"]}', session) for link in category_links]
        result = await asyncio.gather(*tasks)
        print(sum(result))


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)

#EXAMPLE
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from aiohttp_retry import RetryClient

URL = 'https://parsinger.ru/asyncio/create_soup/1/index.html'
BASE = 'https://parsinger.ru/asyncio/create_soup/1/'
# Сбор ссылок провожу обычным линейным способом
html = requests.get(URL).text
soup = BeautifulSoup(html, "html.parser")
links = [BASE + x['href'] for x in soup.find_all('a', href=True)]
result = []
count = []


async def get_data(sesion, link):
    async with sesion.get(link) as response:
        if response.ok:
            soup = BeautifulSoup(await response.text(), "html.parser")
            result.append(int(soup.find(class_='text').string))
            # Проверка, что все четыре числа найдены
            if len(result) == 4:
                print(f'Проверено ссылок: {len(count)}')
                print(f'Результат: {sum(result)}')
                # Отмена оставшихся задач
                [task.cancel() for task in asyncio.all_tasks() if task.get_name() != "Task-1"]
        else:
            count.append(1)


async def main():
    async with aiohttp.ClientSession() as session:
        retry_client = RetryClient(client_session=session)
        await asyncio.gather(*[get_data(retry_client, link) for link in links], return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())