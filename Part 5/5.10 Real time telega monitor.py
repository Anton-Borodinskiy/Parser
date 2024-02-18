from pyrogram import Client, filters
import asyncio

# Укажите свои API ID и API Hash для подключения к Telegram API
api_id = 2 ** ** ** *2
api_hash = "8****************7"

# Создание клиента Pyrogram для взаимодействия с Telegram
app = Client("my_session", api_id=api_id, api_hash=api_hash)

# Список чатов, в которых будет производиться поиск сообщений
chats = ['ru_python', 'python_scripts', 'moscowpythonconf', 'rudepython', 'pythonchatru',
         'python_academy_chat', 'python_noobs', 'pythontalk_chat', 'pythonguruchat',
         'Python', 'pydjango', 'ChatPython', 'ru_python_beginners', 'karpovcourseschat']

# Список ключевых слов для поиска в сообщениях
words = ['.', ',']


# Функция для проверки сообщений на наличие ключевых слов
async def check_message(client, message):
    for word in words:
        if word in message.text:
            # Формирование ссылки на чат и информации об отправителе
            chat_link = f"https://t.me/{message.chat.username}" if message.chat.username else "Приватный чат"
            sender = f"@{message.from_user.username}" if message.from_user.username else "Неизвестный отправитель"

            # Формирование текста сообщения
            text = f"Чат: {chat_link}\nНайдена фраза: {word}\nОтправитель: {sender}\nСообщение полностью: {message.text}"
            print(text)

            # Отправка сообщения в чат @username
            await client.send_message('@username', text)

            # Установка реакции "палец вверх" через 5 секунд
            await asyncio.sleep(5)
            await client.send_reaction(message.chat.id, message.id, "👍")


# Обработчик для отслеживания новых сообщений в указанных чатах
@app.on_message(filters.chat(chats) & filters.text)
async def message_handler(client, message):
    await check_message(client, message)


# Запуск клиента для мониторинга сообщений
app.run()