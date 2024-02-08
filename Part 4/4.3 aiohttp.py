import time
#EXAMPLE4
import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector, ProxyType


async def main():
    url = 'http://httpbin.org/ip'
    connector = ProxyConnector(
            proxy_type=ProxyType.SOCKS5,
            host='194.28.210.39',
            port=9867,
            username='D2Frs6',
            password='75JjrW',
            rdns=True
            )

    async with aiohttp.ClientSession(connector=connector, timeout=.5, trust_env=True) as session:
        async with session.get(url=url, timeout=1) as response:
            if response.status:
                print(f'good proxy, status_code -{response.status}-', end='')
            elif response.status >= 400:
                print(f'bad proxy, status_code -{response.status}-', end='')


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

#EXAMPLE3
import time
import aiohttp
import asyncio
import aiofiles

url = 'http://httpbin.org/ip'


async def check_proxy(prx, semaphore):
    proxy = f'http://{prx}'
    async with semaphore:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, proxy=proxy, timeout=1) as response:
                    if response.ok:
                        return f'good proxy, status_code: {response.status}, {prx}'
                    else:
                        return f'bad proxy, status_code: {response.status}, {prx}'
        except Exception as e:
            return f'bad proxy, Error: {e.__class__.__name__}, {prx}'


async def main():
    # Внимание! Этот оператор ограничивает количество одновременно выполняемых задач
    # Если код падает с ошибкой ValueError: too many file descriptors in select(),
    # уменьшите это число
    semaphore = asyncio.BoundedSemaphore(500)

    async with aiofiles.open('proxy.txt', mode='r', encoding='utf8') as f:
        # Получаем список прокси из файла
        proxies = await f.readlines()
        # Создаем и асинхронно запускаем список задач на проверку прокси
        tasks = [check_proxy(prx.strip(), semaphore) for prx in proxies]
        # Ждем, пока выполнятся все проверки
        result = await asyncio.gather(*tasks, return_exceptions=True)
        # Выводим результат проверки
        print(f"Всего проверено: {len(result)} шт.")
        print(*result, sep='\n')


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
start = time.time()
asyncio.run(main())
print(f'Затрачено времени: {time.time() - start} секунд')


#EXAMPLE2
import aiohttp
import asyncio

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = 'http://httpbin.org/get'
data = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url=url, headers=headers, timeout=1, params=data) as response:
            print(await response.text())


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

time.sleep(40)
#EXAMPLE1
import aiohttp
import asyncio

async def main():
#------------------------------------start block 2------------------------------------

    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get('https://parsinger.ru/html/index1_page_1.html') as response:
            print(await response.text())

#------------------------------------end block 2------------------------------------


#------------------------------------start block 1------------------------------------

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

#------------------------------------start block 1------------------------------------