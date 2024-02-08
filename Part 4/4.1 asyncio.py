#EXAMPLE5
import asyncio
import random


async def two(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def one(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def main():
    for x in range(5):
        task1 = asyncio.create_task(one(1))
        task2 = asyncio.create_task(two(2))
        await task1
        await task2
asyncio.run(main())

#EXAMPLE4
import asyncio
import time


async def two():
    print('world')

async def three():
    await asyncio.sleep(5)
    print('test')

async def one():
    print('hello')
    await asyncio.sleep(1)
    await three()
    await two()
    print('end!')


asyncio.run(one())

#EXAMPLE3
import asyncio


async def nested(text, number):
    return print(text, number)


async def main():
    task = asyncio.create_task(nested('Переданное число', 333))
    await task


asyncio.run(main())

#EXAMPLE2
import asyncio
import aiohttp
from codetiming import Timer

#---------------------start block 1------------------------
urls = ["http://google.com",
        "http://yahoo.com",
        "http://apple.com",
        "http://microsoft.com",
        "https://habr.com/",
        "https://www.youtube.com/",
        "https://stepik.org/",
        "https://docs.python.org/",
        "https://stackoverflow.com/",
        "https://www.reg.ru/"]
#---------------------end block 1------------------------



#---------------------start block 2------------------------
async def main(url):
    with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.url)
#---------------------end block 2------------------------



#---------------------start block 3------------------------
if __name__ == '__main__':
    task = [main(link) for link in urls]
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(asyncio.wait(task))
#---------------------end block 3------------------------




#EXAMPLE1
import asyncio
import aiohttp
from codetiming import Timer

#---------------------start block 1------------------------
urls = ["http://google.com",
        "http://yahoo.com",
        "http://apple.com",
        "http://microsoft.com",
        "https://habr.com/",
        "https://www.youtube.com/",
        "https://stepik.org/",
        "https://docs.python.org/",
        "https://stackoverflow.com/",
        "https://www.reg.ru/"]
#---------------------end block 1------------------------



#---------------------start block 2------------------------
async def main(url):
    with Timer(text=f"Затрачено времени на запрос: {{:.3f}} сек"):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                print(resp.url)
#---------------------end block 2------------------------


async def run_tasks():
    tasks = [main(link) for link in urls]
    await asyncio.gather(*tasks)

#---------------------start block 3------------------------
if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(run_tasks())
#---------------------end block 3------------------------