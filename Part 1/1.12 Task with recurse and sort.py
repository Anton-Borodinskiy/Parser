import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Отправляем GET-запрос
r = requests.get('https://parsinger.ru/3.4/2/index.html')
# Изменить кодировку
r.encoding = 'utf-8'
# print(r.text)

response = requests.get('https://parsinger.ru/img_download/index.html')
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
imgs = soup.findAll('img')
# for img in imgs:
#     print(img["src"])
#     response = requests.get(f'https://parsinger.ru/img_download/{img["src"]}')
    # with open(f'{img["src"]}'.split("/")[-1], 'wb') as file:
    #     file.write(response.content)


response = requests.get('https://parsinger.ru/3.4/1/json_weather.json')
wea_data = response.json()
# pprint(wea_data)
coldest = None
# for i in range(len(wea_data)):
#     if coldest is None or coldest > int(wea_data[i]['Температура воздуха'].split("°")[0]):
#         coldest = int(wea_data[i]['Температура воздуха'].split("°")[0])
#         date_of_cold = wea_data[i]["Дата"]
# print(date_of_cold)
list_with_all = []
def unpack_comment(to_unpack):
    if len(to_unpack['comments']) == 0:
        list_with_all.append(to_unpack)
    else:
        list_with_all.append(to_unpack)
        for i in range(len(to_unpack['comments'])):
            unpack_comment(to_unpack['comments'][i])


response = requests.get('https://parsinger.ru/3.4/3/dialog.json')
comments_user = response.json()
unpack_comment(comments_user)
final_dict = {}
for i in range(len(list_with_all)):
    if list_with_all[i]['username'] in final_dict:
        final_dict[list_with_all[i]['username']] += 1
    else:
        final_dict[list_with_all[i]['username']] = 1

sorted_final_dict = sorted(final_dict.items(), key=lambda x: (-x[1], x[0]))
pprint(sorted_final_dict)
converted_dict = dict(sorted_final_dict)
print(converted_dict)

