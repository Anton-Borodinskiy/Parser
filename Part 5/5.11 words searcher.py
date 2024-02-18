from pyrogram import Client
import json
import asyncio


api_id = 2**********2
api_hash = "8*****************7"


# Список чатов и ключевых слов
chats = ['ru_python', 'python_scripts','moscowpythonconf', 'rudepython', 'pythonchatru',
         'python_academy_chat', 'python_noobs', 'pythontalk_chat', 'pythonguruchat',
         'Python', 'pydjango', 'ChatPython', 'ru_python_beginners','karpovcourseschat']
words = ['pyrogram']


# Асинхронная функция для проверки наличия ключевых слов в сообщении
async def contains_keywords(message, keywords):
    if message:
        # Возвращает словарь, где ключи - это слова, а значения - True или False в зависимости от того, найдено ли слово в сообщении
        return {word: word in message.lower() for word in keywords}
    # Если сообщение отсутствует, возвращает словарь с False для всех слов
    return {word: False for word in keywords}

# Асинхронная функция для сохранения данных в формате JSON
async def save_to_file(data, filename='saved_messages.json'):
    with open(filename, 'a', encoding='utf-8') as f:
        # Запись данных в файл в формате JSON
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Сообщение сохранено в файл:", data)

# Асинхронная функция для создания ссылки на сообщение
def create_message_link(chat, message_id):
    return f"https://t.me/{chat}/{message_id}"

# Основная асинхронная функция для работы со скриптом
async def main():
    # Инициализация асинхронного клиента Pyrogram
    async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
        # Проход по списку чатов
        for chat in chats:
            print(f"Проверка чата: {chat}")
            messages_count = 0
            # Асинхронное получение истории сообщений из чата
            async for message in app.get_chat_history(chat, limit=1000):
                messages_count += 1
                # Проверка сообщения на наличие ключевых слов
                keywords_found = await contains_keywords(message.text, words)
                # Если в сообщении найдено ключевое слово
                if message.text and any(keywords_found.values()):
                    # Создание ссылки на сообщение
                    message_link = create_message_link(chat, message.id)

                    # Сбор данных о сообщении
                    data = {
                        "Чат": chat,
                        "Найдена фраза": keywords_found,
                        "Отправитель": f"@{message.from_user.username}" if message.from_user else "Неизвестно",
                        "Дата отправки": str(message.date),
                        "Сообщение полностью": message.text,
                        "Ссылка на сообщение": message_link,
                    }
                    # Сохранение данных в файл
                    await save_to_file(data)
            print(f"Всего обработано сообщений в чате '{chat}': {messages_count}")

