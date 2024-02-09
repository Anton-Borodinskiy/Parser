#EXAMPLE1

import time
import aiofiles
import asyncio


# Этот код читает файл построчно миллион строк.
async def gen_numbers():
    async with aiofiles.open('async_write_one_millon_numbers.txt', mode='r') as file:
        text = await file.readline()
        print(text)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gen_numbers())
print(time.perf_counter() - start)


import time
import aiofiles
import asyncio


# Этот код читает файл построчно миллион строк.
async def gen_numbers():
    async with aiofiles.open('async_write_one_millon_numbers.txt', mode='r') as file:
        text = await file.readlines()
        print(text)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(gen_numbers())
print(time.perf_counter() - start)

# Этот код генерирует и записывает в файл целиком миллион чисел от 100к до 1кк

import time
import aiofiles
import asyncio


async def write_numbers():
    async with aiofiles.open('async_write_one_millon_numbers.txt', mode='w') as file:
        numbers = str([x for x in range(100000, 1000001)])
        await file.write(numbers)


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(write_numbers())
print(time.perf_counter() - start)

#Этот код генерирует и записывает в файл построчно 100к ранодмных чисел от 10к до 100к

import time
import aiofiles
import asyncio
import random


async def write_numbers():
    async with aiofiles.open('one_millon_numbers.txt', mode='a') as file:
        for x in range(1, 100000):
            await file.writelines(str(random.randint(10000, 100000)) + '\n')


start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(write_numbers())
print(time.perf_counter() - start)

