import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/table/1/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')
rows = table.find_all('tr')[1:]
all_numbers = []
for i in range(len(rows)):
    columns = rows[i].find_all(['td', 'th']) # Один из двух td/th
    for col in columns:
        all_numbers.append(float(col.text))

all_numbers = list(set(all_numbers))
print(sum(all_numbers))

#PART 2

url = 'https://parsinger.ru/table/2/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')
rows = table.find_all('tr')[1:]
all_numbers = []
for i in range(len(rows)):
    columns = rows[i].find_all(['td', 'th'])[0] # Один из двух td/th
    for col in columns:
        all_numbers.append(float(col.text))


print(sum(all_numbers))

#PART 3
url = 'https://parsinger.ru/table/3/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
rows = soup.find_all('b')
sum_all = 0
for row in rows:
    sum_all += float(row.text)
print(sum_all)

#PART 4
url = 'https://parsinger.ru/table/4/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
rows = soup.find_all(class_="green")
sum_all = 0
for row in rows:
    sum_all += float(row.text)
print(sum_all)

#PART 5
url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')
rows = table.find_all('tr')[1:]
all_numbers = []
sum_all = 0
for i in range(len(rows)):
    columns = rows[i].find_all(['td', 'th']) # Один из двух td/th
    for col in columns:
        if col.get('class'):
            first_dig = float(col.text)

    sum_all += first_dig * int(columns[-1].text)
print(sum_all)

#PART 6
url = 'https://parsinger.ru/table/5/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')
rows = table.find_all('tr')[1:]
final_dict = {}
for i in range(len(rows[0].find_all(['td', 'th']))):
    final_dict[f"{i+1} column"] = 0

for i in range(len(rows)):
    columns = rows[i].find_all(['td', 'th']) # Один из двух td/th
    for k in range(len(columns)):
        final_dict[f"{k + 1} column"] += float(columns[k].text)


for fin in final_dict:
    final_dict[fin] = round(final_dict[fin], 3)

print(final_dict)

#PART 7
url = 'https://parsinger.ru/4.8/7/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table')
sum_of_3 = 0
for tab in table:
    rows = tab.find_all('tr')
    for row in rows:
        columns = row.find_all(['td', 'th'])
        for col in columns:
            if int(col.text)%3 == 0:
                sum_of_3 += int(col.text)
print(sum_of_3)