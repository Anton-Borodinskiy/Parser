from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

emails = soup.select('.email_field')
all_mails = []
for em in emails:
    all_mails.append(em.strong.next_sibling.strip())
print(all_mails)

# # Нахождение всех блоков с электронной почтой
# email_blocks = soup.find_all('div', class_='email_field')
#
# # Извлечение адресов электронной почты
# emails = [block.strong.next_sibling.strip() for block in email_blocks]

# emails = soup.select('.email_field strong')
# emails = [tag.next_sibling.strip() for tag in emails]