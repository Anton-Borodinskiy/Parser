from pyrogram import Client, filters
from pyrogram.enums import MessagesFilter
from pyrogram.types import MessageEntity
import yaml
from pyrogram.enums import MessagesFilter, MessageServiceType
import time
#TASK4
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        all_online = []
        for message in messages:
            if message.reply_to_message_id:
                all_online.append(message.reply_to_message_id)
        sum_id = []
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        for message in messages:
            if message.id in all_online:
                print(message.id)
                sum_id.append(message.from_user.id)
        print(sum(set(sum_id)))
main()
time.sleep(500)
#EXAMPLE
#
# from pyrogram import Client
# from pyrogram.enums import MessagesFilter
#
# api_id = 2********2
# api_hash = "8********************"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# res = []
# group_url = "parsinger_pyrogram"  # URL группы
#
#
# def main():
#     with app:
#         messages = app.get_chat_history(group_url)  # Получение истории чата
#         reply_info_list = []
#         original_message_users = set()  # Множество для хранения уникальных ID пользователей
#
#         for message in messages:
#             if message.reply_to_message_id and (original_message := app.get_messages(group_url, message.reply_to_message_id)).from_user:
#                 user_id, username, original_text = original_message.from_user.id, original_message.from_user.username, original_message.text
#                 reply_info_list.append((user_id, username, original_text))
#                 original_message_users.add(user_id)
#
#         # Вывод информации об ответах и ID пользователей, сделавших оригинальные сообщения
#         print("Информация об ответах:\n", *reply_info_list, "\n\nID пользователей, сделавших оригинальные сообщения:\n", *original_message_users, "\nСумма ID: ", sum(original_message_users))
#
# main()

#TASK3
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        all_online = {}
        for message in messages:
            if message.from_user:
                if message.from_user.last_online_date:
                    all_online[message.from_user.id] = message.from_user.last_online_date
        print(sorted(all_online.items(), key=lambda x: x[-1]))
main()
time.sleep(500)
#EXAMPLE
# from pyrogram import Client
# from pypyro import api_id, api_hash
#
# group_url = "parsinger_pyrogram"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
#
#
# # def main():
# #     with app:
# #         messages = app.get_chat_history(chat_id=group_url)
# #         # Стандартный вывод сообщений идет в очередности от новейшего к старейшему.
# #         # Разворачиваю очередность, теперь, даже если у пользователя было несколько сообщений
# #         # в словаре сможет сохраниться только дата самого свежего сообщения.
# #         dct = {mfu.id: mfulod for message in [*messages][::-1]
# #                if (mfu := message.from_user) and (mfulod := mfu.last_online_date)}
# #         print(min(dct, key=dct.get))


main()
#TASK2
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.search_messages(group_url, filter=MessagesFilter.PINNED)  # Получаем историю чата для указанной группы
        len_of_all =0
        for message in messages:
            if message.text:
                len_of_all += len(message.text.replace(" ",""))
        print(len_of_all)


main()
time.sleep(500)
#TASK1
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        sum_of_gif = []
        for message in messages:
            if message.animation:
                print(message.id)
                print(message.from_user.id)
                sum_of_gif.append(int(message.id) * int(message.from_user.id))
        print(sum(sum_of_gif))


main()

#EXAMPLE TASK1
# from pyrogram import Client
# from pyrogram.enums import MessagesFilter
#
# api_id = 2**********2
# api_hash = "8*******************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# res = []
#
#
# def main():
#     with app:
#         group_url = "parsinger_pyrogram"
#         messages = app.search_messages(group_url,
#                                        filter=MessagesFilter.ANIMATION)  # Получаем историю чата для указанной группы
#         for message in messages:
#             res.append(message.from_user.id * message.id)
#             print(message.from_user.id * message.id)
#
#
# main()
# print(sum(res))

# MessageEntityType.MENTION: Упоминание пользователя с @username
# MessageEntityType.HASHTAG: Хештег с #hashtag
# MessageEntityType.CASHTAG: Кэштег с $USD
# MessageEntityType.BOT_COMMAND: Команда бота, например /start@pyrogrambot
# MessageEntityType.URL: URL-адреса, например https://pyrogram.org
# MessageEntityType.EMAIL: Электронная почта, например do-not-reply@pyrogram.org
# MessageEntityType.PHONE_NUMBER: Номер телефона, например +1-123-456-7890
# MessageEntityType.BOLD: Жирный текст
# MessageEntityType.ITALIC: Курсивный текст
# MessageEntityType.UNDERLINE: Подчеркнутый текст
# MessageEntityType.STRIKETHROUGH: Текст с зачеркиванием
# MessageEntityType.SPOILER: Текст спойлера
# MessageEntityType.CODE: Строка моноширинного шрифта
# MessageEntityType.PRE: Блок моноширинного шрифта (с указанием языка)
# MessageEntityType.BLOCKQUOTE: Текст цитаты
# MessageEntityType.TEXT_LINK: Для кликабельных текстовых URL
# MessageEntityType.TEXT_MENTION: Для упоминания пользователей без имени пользователя (с указанием пользователя)
# MessageEntityType.BANK_CARD: Текст банковской карты
# MessageEntityType.CUSTOM_EMOJI: Пользовательские эмодзи
# MessageEntityType.UNKNOWN: Неизвестный тип сущности сообщения

# {
#     "_": "MessageEntity",   # Это поле обозначает тип объекта, в данном случае, это "MessageEntity".
#     "type": "MessageEntityType.CUSTOM_EMOJI", # Указывает на тип сущности, в данном случае, это пользовательский эмодзи (CUSTOM_EMOJI).
#     "offset": 24,           # Смещение сущности в тексте сообщения, начиная с 24-го символа в кодировке UTF-16.
#     "length": 2,            # Длина сущности, занимает 2 символа в тексте сообщения.
#     "custom_emoji_id": 5337310516769467285    # Уникальный идентификатор пользовательского эмодзи.
# },
# {
#     "_": "MessageEntity",
#     "type": "MessageEntityType.URL",
#     "offset": 0,
#     "length": 33
# }



# with open('telega.yaml', 'r') as file:
#     creds = yaml.safe_load(file)
# api_id = creds["api_id"]
# api_hash = creds["api_hash"]
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
#
# def main():
#     with app:
#         group_url = "parsinger_pyrogram"
#         messages = app.search_messages(group_url)
#         for message in messages:
#             print(message)
#
#
# main()