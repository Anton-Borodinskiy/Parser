import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import csv



url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
#TASK 1
dict_of_items = {}
for i in range(len(response)):
    if response[i]["categories"] in dict_of_items:
        dict_of_items[response[i]["categories"]] += int(response[i]["count"])
    else:
        dict_of_items[response[i]["categories"]] = int(response[i]["count"])
print(dict_of_items)

#TASK2
dict_of_items = {}
for i in range(len(response)):
    if response[i]["categories"] in dict_of_items:
        dict_of_items[response[i]["categories"]] += int(response[i]["count"]) * int(response[i]["price"].split()[0])
    else:
        dict_of_items[response[i]["categories"]] = int(response[i]["count"]) * int(response[i]["price"].split()[0])
print(dict_of_items)

#TASK3
url = 'https://parsinger.ru/4.6/1/res.json'

response = requests.get(url=url).json()
dict_of_items = {}
for i in range(len(response)):
    if response[i]["categories"] in dict_of_items:
        dict_of_items[response[i]["categories"]] += int(response[i]["article"]) * int(response[i]["description"]["rating"])
    else:
        dict_of_items[response[i]["categories"]] = int(response[i]["article"]) * int(response[i]["description"]["rating"])
print(dict_of_items)