# app.get_chat_history(chat_id, limit=100, offset_id=0, offset_date=None): Используется для получения истории чата. Её параметры позволяют настраивать, какие сообщения и в каком объеме вы хотите извлечь.
# Вот подробное описание параметров:
# chat_id: идентификатор чата или его имя пользователя.
# limit: максимальное количество сообщений для извлечения (максимум 100 за один вызов).
# offset_id: идентификатор сообщения, с которого начнется извлечение (используется для пагинации).
# offset_date: дата, с которой начнется извлечение сообщений.


#TASK1
from pyrogram import Client
import yaml

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
group_url = "parsinger_pyrogram"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

def member_ex():
    with app:
        chat = app.get_chat_history(group_url)
        all_gitis = []
        for message in chat:
            if message.text and message.text.isdigit():
                all_gitis.append(int(message.text) * int(message.id))
        print(sum(all_gitis))
member_ex()

# Перед запуском кода, вставьте свои значения в api_id и api_hash

from pyrogram import Client
import yaml

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]

app = Client("my_session", api_id=api_id, api_hash=api_hash)


# Получаем историю чата
def main():
    with app:
        group_url = "python_parsing"
        messages = app.get_chat_history(group_url, limit=1)
        for message in messages:
            print(message)


main()