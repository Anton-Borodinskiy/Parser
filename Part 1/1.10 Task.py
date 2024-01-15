import requests
# sum = 0
# for i in range(200):
#     url = f"https://parsinger.ru/3.3/2/{i+1}.html"
#     response = requests.get(url=url)
#     sum+= response.status_code
# print(sum)


# for i in range(200):
#     url = f"https://parsinger.ru/3.3/1/{i+1}.html"
#     response = requests.get(url=url)
#     if response.status_code == 200:
#         print(response.text)

# name_img= ['1663231240183817644.jpg',
#  '1663231245165469794.jpg',
#  '1663231252148267596.jpg',
#  '16632460271311817.jpg',
#  '1663260860165832550.jpg',
#  '1663260862112644405.jpg',
#  '1663260864114071369.jpg',
#  '1663260869127473152.jpg',
#  '1663260874115452216.jpg',
#  '1663260877136512181.jpg',
#  '1663260878140464277.jpg',
#  '1663267600193799276.jpg',
#  '1663267613117130673.jpg',
#  '1663267619197170483.jpg',
#  '1663267626154597739.jpg',
#  '1663267648135114690.jpg',
#  '166326765416196421.jpg',
#  '1663267662118079649.jpg',
#  '1663267668165066872.jpg',
#  '1663267878176341940.jpg',
#  '166326990115068678.jpg',
#  '1663269922185881885.jpg',
#  '1663269927127433209.jpg',
#  '1663269942143420441.jpg',
#  '1663269946174943071.jpg',
#  '1663269964195277579.jpg',
#  '1663269970148058649.jpg',
#  '1663269974197750992.jpg',
#  '166326997917397750.jpg',
#  '1663270039138442380.jpg',
#  '1663388012194470737.jpg',
#  '166342371029995280.jpg',
#  '1663423712288242036.jpg',
#  '1663423715255612089.jpg',
#  '1663423720221155166.jpg',
#  '1663423722211139858.jpg',
#  '1663423724211218483.jpg',
#  '1663423728215479371.jpg',
#  '1663423729298828299.jpg',
#  '1663423732225964403.jpg',
#  '1663424198111663025.jpg',
#  '1663424199157537861.jpg',
#  '1663424200184778832.jpg',
#  '166342420214123494.jpg',
#  '166342420317539591.jpg',
#  '1663424204161674559.jpg',
#  '1663424206188873432.jpg',
#  '166342420813193185.jpg',
#  '1663424209187179962.jpg',
#  '1663424212162573102.jpg']
#
# len_i = 0
# for img in name_img:
#     url = f"https://parsinger.ru/3.3/3/img/{img}"
#     response = requests.get(url=url)
#     if int(response.headers.get('Content-Length')) > len_i:
#         len_i = int(response.headers.get('Content-Length'))
#         found_url = url
# print(found_url)
list_of_availible = []
for i in range(100):
    url = f"https://parsinger.ru/3.3/4/{i+1}.html"
    response = requests.get(url=url)
    if response.status_code == 200:
        list_of_availible.append(url.split("/")[-1])

print(f"Первая доступная страница: {list_of_availible[0]}")
print(f"Последняя доступная страница: {list_of_availible[-1]}")
