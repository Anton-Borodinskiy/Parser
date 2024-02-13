#TASK 1
from pyrogram import Client
import yaml
from pyrogram.enums import MessagesFilter

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
group_url = "parsinger_pyrogram"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

def member_ex():
    with app:
        all_ids = []
        messages = app.search_messages(chat_id=group_url)
        for message in messages:
            if message.text and "https:" not in message.text:
                pass
            elif not message.text:
                pass
            else:
                print(message.text)
                all_ids.append(int(message.id))
        print(sum(all_ids))
member_ex()

#EXAMPLE
group_url = "parsinger_pyrogram"
messages = app.search_messages(group_url, filter=MessagesFilter.URL)
for message in messages:
    # Проверяем, что текст сообщения существует перед поиском 'http'
    if message.text and 'http' in message.text:
        print(message.id)
        res.append(message.id)

# app.search_messages(chat_id, query, offset, filter, limit, from_user)
#
# chat_id(int | str) - Это номер или имя пользователя чата, в котором вы хотите искать сообщения. Если вы хотите искать в своих сохраненных сообщениях, используйте "me" или "self".,
#
# query(str, необязательный) - Это слово или фраза, которую вы хотите найти в сообщениях. Если вы ищете фотографии или видео, этот параметр поможет найти те, у которых есть подписи с этим текстом.
#
# offset(int, необязательный) - Это стартовая точка поиска. Если вы поставите 0, поиск начнется с самого первого сообщения. Если вы поставите 10, поиск начнется с 11-го сообщения.
#
# filter(enums.MessagesFilter, необязательный) - Это специальный фильтр, который позволяет вам искать определенные типы сообщений, например, только фотографии или только видео.
#
# limit(int, необязательный) - Это максимальное количество сообщений, которые вы хотите получить. Если вы не укажете этот параметр, поиск вернет все подходящие сообщения.
#
# from_user(int | str, необязательный) - Это номер или имя пользователя человека, чьи сообщения вы хотите найти. Если вы хотите найти сообщения, которые вы отправили, используйте me или self.

#EXAMPLE

# from pyrogram import Client
#
# api_id = 2********2
# api_hash = "8*****************7"
#
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
#
# chat_id = 'python_parsing'  # Например, можно использовать @username для публичных каналов или чатов
# query = 'парсинг'           # Текст, который вы хотите найти в сообщениях
# offset = 0                  # Смещение от начала списка сообщений (0 означает начало)
# filter = None               # Тип фильтра (например, 'photo' для фото)
# limit = 200                 # Максимальное количество сообщений, которое вы хотите получить
# from_user = 'Pashikk'       # Если нужно искать сообщения только от конкретного пользователя
#
#
# def main():
#     with app:
#         # Поиск сообщений
#         messages = app.search_messages(chat_id=chat_id, query=query, offset=offset, limit=limit, from_user=from_user)
#         # Вывод результатов
#         for message in messages:
#             print(message.from_user.username, message.text)  # Вывод ID сообщения и его текста
#
#
# main()

#FILTERS
#
# with Client("my_account") as app:
#     # Пустой фильтр (любой тип сообщений)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.EMPTY)
#
#     # Сообщения с фотографиями
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO)
#
#     # Сообщения с видео
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO)
#
#     # Возвращает сообщения, содержащие либо фотографии, либо видео
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO_VIDEO)
#
#     # Возвращает сообщения, содержащие документы (например, PDF, DOCX)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.DOCUMENT)
#
#     # Сообщения, содержащие URL-адреса
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.URL)
#
#     # Возвращает сообщения, содержащие анимации (обычно это GIF).
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.ANIMATION)
#
#     # Сообщения с голосовыми заметками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VOICE_NOTE)
#
#     # Сообщения с видеозаметками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO_NOTE)
#
#     # Возвращает сообщения, содержащие аудио и видеозаметки
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO_VIDEO_NOTE)
#
#     # Аудиосообщения (музыка)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO)
#
#     # Сообщения с фотографиями чата
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CHAT_PHOTO)
#
#     # Сообщения с телефонными звонками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHONE_CALL)
#
#     # Возвращает сообщения, в которых есть упоминания пользователя (через @username или если пользователь упомянут напрямую).
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.MENTION)
#
#     # Сообщения с местоположением
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.LOCATION)
#
#     # Сообщения с контактами
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CONTACT)
#
#     # Закрепленные сообщения
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PINNED)