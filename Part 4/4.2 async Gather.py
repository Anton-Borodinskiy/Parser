#EXAMPLE4
import asyncio
import random


async def one(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def main():
    lst = [x for x in range(10)]
    lst_tasks = []
    for x in lst:
        task = asyncio.create_task(one(x))
        lst_tasks.append(task)
    await asyncio.wait(lst_tasks)


asyncio.run(main())

import time
time.sleep(30)
#EXAMPLE3
import asyncio
import random
import time


async def one(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def two(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def three(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def main():
    group1 = asyncio.gather(*[one(i) for i in range(1, 10)])
    group2 = asyncio.gather(*[two(i) for i in range(1, 10)])
    group3 = asyncio.gather(*[three(i) for i in range(1, 10)])

    await asyncio.gather(group1, group2, group3)


asyncio.run(main())


time.sleep(40)
#EXAMPLE2
import asyncio
import random
import time


async def one(x):
    await asyncio.sleep(random.randint(1, 3))
    print(x)


async def main():
    lst = [x for x in range(10)]
    lst_tasks = []
    for x in lst:
        task = asyncio.create_task(one(x))
        lst_tasks.append(task)
    await asyncio.gather(*lst_tasks)


asyncio.run(main())

time.sleep(40)
#EXAMPLE1
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
        await asyncio.gather(one(1), two(2))


asyncio.run(main())