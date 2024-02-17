from pyrogram import Client, filters
from pyrogram.enums import MessagesFilter
from pyrogram.types import MessageEntity
import yaml
from pyrogram.enums import MessagesFilter, MessageServiceType
import time
#TASK1
import os
from tqdm import tqdm

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

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)
api_id = creds["api_id"]
api_hash = creds["api_hash"]
app = Client("my_session", api_id=api_id, api_hash=api_hash)
def progress(current, total, progress_bar):
    # Обновляем прогресс-бар
    progress_bar.update(current - progress_bar.n)

def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        for message in messages:
            if message.media:
                if message.photo:
                    file_name = f"media/{message.id}"
                    file_name += ".jpg"
                    file_size = message.photo.file_size
                    if file_size:
                        with tqdm(total=file_size, unit='B', unit_scale=True, desc="Скачивание") as progress_bar:
                            app.download_media(message, file_name=file_name, progress=progress, progress_args=(progress_bar,))

        print(calculate_directory_size("media"))

main()
time.sleep(500)

#EXAMPLE
# import time
#
# from pyrogram import Client
# from pypyro import api_id, api_hash
# from pyrogram.enums import MessagesFilter
# import os
# import asyncio
#
# group_url = "parsinger_pyrogram"
#
#
# def calculate_directory_size(path):
#     size_byte = 0
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 size_byte += os.path.getsize(file_path)
#     return size_byte
#
#
# async def downloader(app, message):
#     await app.download_media(message.photo, file_name=f'photo/{message.id}.jpg')
#
#
# async def main():
#     async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
#         tasks = [downloader(app, message) async for message in
#                  app.search_messages(chat_id=group_url, filter=MessagesFilter.PHOTO)]
#         await asyncio.gather(*tasks)
#
#
# start = time.time()
# asyncio.run(main())
# print(f'Время скачивания фото: {time.time() - start}')
# print(calculate_directory_size('photo'))

#DOWNLOAD FILES
# from pyrogram import Client
# from tqdm import tqdm
#
# api_id = 2*********2
# api_hash = "8*****************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# group_url = "python_parsing"  # URL группы
#
# def progress(current, total, progress_bar):
#     # Обновляем прогресс-бар
#     progress_bar.update(current - progress_bar.n)
#
# def main():
#     with app:
#         for message in app.get_chat_history(group_url):
#             if message.media:
#                 file_name = f"media/{message.id}"
#                 file_size = None
#
#                 # Определение расширения файла и размера в зависимости от типа медиа
#                 if message.photo:
#                     file_name += ".jpg"
#                     file_size = message.photo.file_size
#                 elif message.video:
#                     file_name += ".mp4"
#                     file_size = message.video.file_size
#                 elif message.audio:
#                     file_name += ".mp3"
#                     file_size = message.audio.file_size
#                 elif message.document:
#                     file_name += f".{message.document.mime_type.split('/')[-1]}"
#                     file_size = message.document.file_size
#                 elif message.voice:
#                     file_name += ".ogg"
#                     file_size = message.voice.file_size
#                 elif message.video_note:
#                     file_name += ".mp4"
#                     file_size = message.video_note.file_size
#                 elif message.sticker:
#                     file_name += ".webp"
#                     file_size = message.sticker.file_size
#                 elif message.animation:
#                     file_name += ".mp4"
#                     file_size = message.animation.file_size
#
#                 # Создание прогресс-бара для каждого файла
#                 # Если размер файла определен, создаем прогресс-бар и начинаем загрузку
#                 if file_size:
#                     with tqdm(total=file_size, unit='B', unit_scale=True, desc="Скачивание") as progress_bar:
#                         app.download_media(message, file_name=file_name, progress=progress, progress_args=(progress_bar,))
#
# main()

# app.download_media(message, file_name, in_memory, block, progress, progress_args)


# message - Это объект сообщения, из которого вы хотите скачать медиа. Сообщение может содержать различные типы медиа, такие как фотографии, видео, аудиофайлы и т.д.
# available_media = ("audio", "document", "photo", "sticker", "animation", "video", "voice", "video_note",
#                    "new_chat_photo")

# file_name - Путь к файлу, куда будет сохранено скачанное медиа. Этот аргумент определяет, куда на вашем устройстве или сервере будет сохранен файл. Если вы укажете просто имя файла, он сохранится в текущей рабочей директории.
# file_name=f"media/{message.message_id}.mp4"

# in_memory - Если этот аргумент установлен в True, медиа будет скачиваться в память (то есть в объект bytes), а не в файл на диске. Это полезно, если вам нужно обработать медиа на лету, не сохраняя его физически.
#
# block - Этот аргумент определяет, будет ли функция блокирующей. Если установлено значение True, выполнение кода остановится, пока медиа не будет полностью скачано. Если False, код продолжит выполняться параллельно скачиванию (для асинхронного выполнения кода).
#
# progress - Функция обратного вызова, которая вызывается для отслеживания прогресса скачивания. Эта функция может использоваться для отображения прогресс-бара или для логирования прогресса скачивания.
# # Функция для обновления прогресс-бара
# def progress(current, total):
#     # 'current' - текущее количество скачанных байт,
#     # 'total' - общий размер файла
#     progress_bar.update(current - progress_bar.n)  # Обновляем прогресс-бар
#
# #...
# #Любое количество кода
# #...
#
#
# app.download_media(message..., file_name=..., progress=progress)

# progress_args - Дополнительные аргументы, которые будут переданы в вашу функцию прогресса. Это может быть что угодно, что поможет вам лучше управлять процессом отслеживания прогресса.

#EXAMPLES

# audio: Аудиофайлы или музыкальные треки.
#
# # Проверка наличия аудио в сообщении
# if message.audio:
#     # Скачиваем аудио
#     app.download_media(message.audio, file_name=f"audio/{message.message_id}.mp3")

# document: Документы, такие как PDF, Word или любые другие файлы, которые не подпадают под другие медиа-категории.
#
# # Проверка наличия документа в сообщении
# if message.document:
#     # Скачиваем документ
#     app.download_media(message.document, file_name=f"documents/{message.message_id}_{message.document.file_name}")

# # Проверка наличия фотографии в сообщении
# if message.photo:
#     # Скачиваем фотографию
#     app.download_media(message.photo, file_name=f"photos/{message.message_id}.jpg")

# # Проверка наличия стикера в сообщении
# if message.sticker:
#     # Скачиваем стикер
#     app.download_media(message.sticker, file_name=f"stickers/{message.message_id}.webp")

# Проверка наличия новой фотографии чата в сообщении
# if message.new_chat_photo:
#     # Скачиваем новую фотографию чата
#     app.download_media(message.new_chat_photo, file_name=f"chat_photos/{message.message_id}.jpg")




# from pyrogram import Client
#
# api_id = 2**********2
# api_hash = "8*****************7"
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
# group_url = "parsinger_pyrogram"  # URL группы
#
#
# def main():
#     with app:
#         for message in app.get_chat_history(group_url):
#             # Проверяем, содержит ли сообщение изображение
#             if message.photo:
#                 # Скачиваем изображение
#                 app.download_media(message.photo, file_name=f"images/{message.from_user.id}_{message.id}.jpg")
#
#
# main()