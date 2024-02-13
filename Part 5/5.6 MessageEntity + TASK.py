from pyrogram import Client, filters
from pyrogram.enums import MessagesFilter
from pyrogram.types import MessageEntity
import yaml
from pyrogram.enums import MessagesFilter

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