from pyrogram import Client, filters
from pyrogram.enums import MessagesFilter
from pyrogram.types import MessageEntity
import yaml
from pyrogram.enums import MessagesFilter, MessageServiceType
import time
import os

def calculate_directory_size(path):
    """
    Подсчитывает размер всех файлов в директории.

    :param path: Путь к директории, размер файлов которой нужно подсчитать.
    :return: Общий размер файлов в байтах.
    """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size
print(calculate_directory_size("media"))
time.sleep(500)
#TASK3
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)
def main():
    with app:
        group_url = "parsinger_pyrogram"
        members = app.get_chat_members(group_url)
        for member in members:
            if member.user:
                print(member)
                if member.user.photo:
                    app.download_media(member.user.photo.big_file_id,f"media/{member.user.id}.jpg")
main()
time.sleep(500)

#TASK2
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)
def main():
    with app:
        group_url = "parsinger_pyrogram"
        numbers_of_math = []
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        for message in messages:
            if message.from_user and message.text:
                if message.from_user.id % 2 == 0 and message.id % 2 == 0 and len(message.text.replace(" ","")) % 2 == 0:
                    numbers_of_math.append(int(message.from_user.id) * int(message.id) * len(message.text.replace(" ","")))
        print(sum(numbers_of_math))



main()
time.sleep(500)
#EXAMPLE
# from pyrogram import Client
#
# api_id = 2*******2
# api_hash = "8****************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# group_url = "parsinger_pyrogram"  # URL группы
# res = []
#
# def find_inactive_users():
#     with app:
#         # Получение списка всех участников чата
#         members = app.get_chat_members(group_url)
#         member_ids = {member.user.id for member in members}
#
#         # Получение истории сообщений чата
#         messages = app.get_chat_history(group_url)
#         for message in messages:
#             # Проверка наличия отправителя и текста сообщения
#             if message.from_user and message.text:
#                 # Проверка на наличие ссылок в сообщении
#                 if "http://" in message.text or "https://" in message.text:
#                     continue  # Пропускаем сообщения с ссылками
#
#                 clear_message = message.text.replace(' ', '')
#
#                 # Проверка на четность ID пользователя, ID сообщения и длины очищенного текста
#                 if message.from_user.id % 2 == 0 and message.id % 2 == 0 and len(clear_message) % 2 == 0:
#                     result = message.from_user.id * message.id * len(clear_message)
#                     print(
#                         f"User ID: {message.from_user.id}, Message_ID:{message.id} COUNT: {len(clear_message)} Message:{clear_message}")
#                     print(f"Result: {result}")
#                     res.append(result)
#
#             # Если отправитель сообщения - участник чата, удаляем его из списка
#             if message.from_user and message.from_user.id in member_ids:
#                 member_ids.remove(message.from_user.id)
#
#         # Оставшиеся в списке - те, кто не отправлял сообщения
#         return member_ids
#
# inactive_user_ids = find_inactive_users()
# print(res)

#TASK1
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)
def main():
    with app:
        group_url = "parsinger_pyrogram"
        id_of_messangers = []
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        for message in messages:
            if message.from_user:
                id_of_messangers.append(message.from_user.id)
        no_messages = []
        members = app.get_chat_members(group_url)
        for member in members:
            if member.user:
                if member.user.id not in id_of_messangers:
                    no_messages.append(member.user.id)

        print(sum(no_messages))


main()
time.sleep(500)
#EXAMPLE
# def main():
#     with app:
#         # Все участики группы
#         members = app.get_chat_members(group_url)
#         all_members = {member.user.id for member in members}
#         # Участники группы, которые писали сообщения
#         messages = app.get_chat_history(group_url)
#         message_users = {messag.from_user.id for messag in messages if messag.from_user}
#         # Разница сумм между двух выборок
#         print(sum(all_members - message_users))
#
# main()

# from pyrogram import Client
#
# api_id = 2**********2
# api_hash = "8******************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
#
#
# def main():
#     with app:
#         user_chat = app.get_users(6833360952)
#         print(user_chat)
#
# main()


# from pyrogram import Client
#
#
# api_id = 2******2
# api_hash = "8****************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# group_url = "parsinger_pyrogram"
#
#
# def main():
#     with app:
#         # Получаем список участников указанной группы (чата). group_url должен быть либо идентификатором чата, либо его URL.
#         members = app.get_chat_members(group_url)
#         for member in members:
#             user_chat = app.get_users(member.user.id)
#             print(user_chat)
#
# main()