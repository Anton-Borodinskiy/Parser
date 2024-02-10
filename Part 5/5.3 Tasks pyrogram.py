from pyrogram import Client
import asyncio
import yaml
from pprint import pprint

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
group_url = "parsinger_pyrogram"
app = Client("my_session", api_id=api_id, api_hash=api_hash)

def member_ex():
    with app:
        chat = app.get_chat_members(group_url)
        all_ids = []
        for member in chat:
            all_ids.append(int(member.user.id))
        print(sum(all_ids))

member_ex()

def title_ex():
    with app:
        chat = app.get_chat(group_url)
        desc_str = chat.description
        for char in desc_str:
            if char.isdigit() and int(char) > 0 and int(char) % 2 == 0:
                print(char,end="")

title_ex()

def photo_ex():
    with app:
        chat = app.get_chat(group_url)

        pprint(chat.photo.big_photo_unique_id)

photo_ex()


#get chat id
def id_ex():
    with app:
        chat = app.get_chat(group_url)

        pprint(chat.id)

id_ex()

