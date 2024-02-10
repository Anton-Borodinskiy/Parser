from pyrogram import Client
import asyncio
import yaml
with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
group_url = "parsinger_pyrogram"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        chat = app.get_chat(group_url)
        print(type(chat))

main()

# chat.id: Уникальный идентификатор чата.
# chat.type: Тип чата (может быть "private", "group", "supergroup" или "channel").
# chat.username: Имя пользователя чата, если это личный чат, или @username канала/супергруппы.
# chat.first_name и last_name: Имя и фамилия пользователя, если это личный чат.
# chat.title: Название группы, супергруппы или канала.
# chat.description: Описание группы, супергруппы или канала.
# chat.pinned_message: Закрепленное сообщение в чате, если оно есть.
# chat.permissions: Права участников чата.
# chat.photo: Фотография профиля чата, если она установлена.