import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
category_links = soup.find("div", class_="nav_menu").find_all("a")
schema = "https://parsinger.ru/html/"
all_pages_of_cat = []
for cat in category_links:
    url = f'{schema}{cat["href"]}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    a_links = soup.find("div", class_="pagen").find_all("a")
    for a in a_links:
        all_pages_of_cat.append(f'{schema}{a["href"]}')
all_pages = []
for page in all_pages_of_cat:
    url = f'{page}'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    all_divs = soup.find_all("div", class_='sale_button')
    for div in all_divs:
        all_pages.append(f'{schema}{div.find("a")["href"]}')
print(all_pages)

async def run_tasks(url, session):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        price = soup.find('span', id='price').text.split()[0]
        old_price = soup.find('span', id='old_price').text.split()[0]
        stock = soup.find('span', id='in_stock').text.split()[-1]
        sale = (int(old_price) - int(price))*int(stock)
        return sale
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(link, session) for link in all_pages]
        result = await asyncio.gather(*tasks)
        sum_of_sale = 0
        for x in result:
            sum_of_sale += x
        print(sum_of_sale)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)

#EXAMPLE
import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup

category_lst = []
pagen_lst = []
domain = 'https://parsinger.ru/html/'
result = []


def get_soup(url):
    resp = requests.get(url=url)
    return BeautifulSoup(resp.text, 'lxml')


def get_urls_categories(soup):
    all_link = soup.find('div', class_='nav_menu').find_all('a')
    for cat in all_link:
        category_lst.append(domain + cat['href'])


def get_urls_pages(category_lst):
    for cat in category_lst:
        resp = requests.get(url=cat)
        soup = BeautifulSoup(resp.text, 'lxml')
        for pagen in soup.find('div', class_='pagen').find_all('a'):
            pagen_lst.append(domain + pagen['href'])


async def get_data(session, link):
    async with session.get(link) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
            for x in item_card:
                url2 = domain + x
                async with session.get(url=url2) as response2:
                    resp2 = await response2.text()
                    soup2 = BeautifulSoup(resp2, 'lxml')
                    old_price = int(soup2.find('span', id='old_price').text.split(" ")[0])
                    price = int(soup2.find('span', id='price').text.split(" ")[0])
                    in_stock = int(soup2.find('span', id='in_stock').text.split(":")[1])
                    result.append(old_price * in_stock - price * in_stock)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for link in pagen_lst:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks)


url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(category_lst)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
print(sum(result))