from pyrogram import Client
import yaml
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        all_messages = []
        for message in app.get_chat_history(group_url, limit=100):
            all_messages.append(message.text)

        # Вывод сообщений на экран или сохранение в файл
        for msg in all_messages:
            print(msg)


main()

#Methods
# 1. Получить информацию о чате

def main():
    with app:
        group_url = "parsinger_pyrogram"
        chat = app.get_chat(group_url)
        print("Chat Info:", chat)

main()

# 2. Получить информацию об участниках чата

def main():
    group_url = "parsinger_pyrogram"
    with app:
        members = app.get_chat_members(group_url, limit=10)
        for member in members:
            print(member.user.first_name, member.user.id)

main()




#Псевдокод для наглядного использование всех параметров
from pyrogram import Client, enums

app = Client("my_account")

def main():
    group_url = "parsinger_pyrogram"  # Имя пользователя или идентификатор чата
    query = "John"           # Строка поиска для фильтрации участников по имени
    limit = 10               # Максимальное количество участников для возврата
    filter = enums.ChatMembersFilter.ADMINISTRATORS  # Фильтр для поиска администраторов чата

    with app:
        members = app.get_chat_members(group_url, query=query, limit=limit, filter=filter)
        for member in members:
            print(member.user.first_name, member.user.id)

if __name__ == "__main__":
    main()

# 3. Получить информацию об участнике чата

def main():
    with app:
        group_url = "parsinger_pyrogram"     # Указываем имя группы или канала
        members = app.get_chat_member(            # Получаем информацию об участнике чата
            chat_id=group_url,                    # ID чата или его имя
            user_id='@HybridAppParser51'               # ID пользователя или его имя пользователя
        )
        print(members)                            # Выводим информацию об участнике чата

main()

# 4. Получить сообщения из чата
def main():
    with app:
        messages = app.get_messages(chat_id="@python_parsing",    # Указываем ID чата для поиска сообщений
                                    message_ids=[123, 456, 789],  # Список ID сообщений, которые мы хотим получить
                                    reply_to_message_ids=[321],   # ID сообщения, на которое были ответы
                                    replies=5)                    # Количество ответов, которые мы хотим получить
        print(messages)                                           # Выводим полученные сообщения

main()


# Псевдокод для демонстрации функции с параметрами

def search_messages_example():
    chat_id = "Parsinger_Telethon_Test"  # Используйте ID чата или его имя пользователя
    query = "hello"  # Текст для поиска в сообщениях
    offset = 0  # Начать с самого первого сообщения
    filter = enums.MessagesFilter.PHOTO  # Искать только сообщения с фотографиями
    limit = 100  # Ограничить результаты поиском первых 100 сообщений
    from_user = "some_user"  # Искать сообщения только от определенного пользователя

    for message in app.search_messages(
            chat_id=chat_id,
            query=query,
            offset=offset,
            filter=filter,
            limit=limit,
            from_user=from_user
    ):
        print(message.text)  # Вывести текст каждого найденного сообщения


# Псевдокод для демонстрации функции с параметрами

def get_history():
    with app:
        chat_id = "parsinger_pyrogram"  # Используйте ID или имя пользователя чата
        limit = 100  # Количество сообщений для получения
        offset = 0  # Смещение относительно первого сообщения в истории
        offset_id = 0  # ID сообщения, с которого начнется получение истории
        offset_date = datetime(2021, 1, 1)  # Получить сообщения, отправленные до 1 января 2021 года

        # Получаем историю чата
        for message in app.get_chat_history(chat_id, limit=limit, offset=offset, offset_id=offset_id,
                                            offset_date=offset_date):
            print(message.text)


get_history()


# Псевдокод для демонстрации функции с параметрами

def main():
    with app:
        chat_id = "username"  # Замените на имя пользователя или ID чата
        chat_photos = app.get_chat_photos(chat_id)

        for photo in chat_photos:
            # Скачиваем каждую фотографию профиля
            app.download_media(photo.file_id, file_name=f"{photo.file_id}.jpg")


main()