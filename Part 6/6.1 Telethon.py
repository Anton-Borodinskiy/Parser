#GET USERS
from telethon import TelegramClient, events, sync, connection
import yaml

with open('telega.yaml', 'r') as file:
    creds = yaml.safe_load(file)

r_api = creds["api_id"]
r_hash = creds["api_hash"]

client = TelegramClient('session_name2', r_api, r_hash)
client.start()

participants = client.get_participants('t.me/Parsinger_Telethon_Test', system_version="4.10.5 beta x64")
print(participants)

# from telethon import TelegramClient, events, sync, connection
# import yaml
#
# with open('telega.yaml', 'r') as file:
#     creds = yaml.safe_load(file)
# api_id = creds["api_id"]
# api_hash = creds["api_hash"]
#
# client = TelegramClient('session_name', api_id, api_hash)
# client.start()
# print(client.get_me())
# client.disconnect()
#
# #METHODS
# #AUTH
# client.start(entity) - запускает клиент (подключается и авторизуется при необходимости), создаёт файл *.session;
# client.send_code_request(entity) - отправляет код Telegram, необходимый для входа на указанный номер телефона;
# client.sign_in(entity) - авторизуется в Telegram под существующей учетной записью пользователя или бота;
# client.qr_login(entity)- инициирует процедуру входа в систему QR;
# client.log_out(entity) - выходит из Telegram и удаляет текущий *.session- файл.
#
# #BASE
# client.connect(entity) - подключается к Телеграму;
# client.disconnect(entity) - отключается от Telegram;
# client.is_connected(entity) - возвращает True, если пользователь подключился;
# client.disconnected(entity) - свойство с a Future, которое разрешается при отключении;
# client.loop(entity) - свойство с asyncio-циклом событий, используемым этим клиентом;
# client.set_proxy(entity) - изменяет прокси, который будет использоваться при следующем (повторном) подключении.
#
# #MESSAGES
# client.send_message(entity) - отправляет сообщение указанному пользователю, чату или каналу;
# client.edit_message(entity) - редактирует данное сообщение, чтобы изменить его текст или медиа;
# client.delete_messages(entity) - удаляет указанные сообщения, опционально «для всех»;
# client.forward_messages(entity) - пересылает данные сообщения указанному объекту;
# client.iter_messages(entity) - итератор по сообщениям для данного чата;
# client.get_messages(entity) - то же , что и iter_messages(), но вместо этого возвращает TotalList;
# client.pin_message(entity) - закрепляет сообщение в чате;
# client.unpin_message(entity) - открепляет сообщение в чате;
# client.send_read_acknowledge(entity) - отмечает сообщения как прочитанные и при необходимости удаляет упоминания.
#
# #FILES
# client.send_file(entity) - отправляет сообщение с данным файлом указанному объекту;
# client.upload_file(entity) - загружает файл на серверы Telegram, не отправляя его.
#
# #DOWNLOAD
# client.download_media(entity) - загружает указанный носитель из объекта сообщения;
# client.download_profile_photo(entity) - загружает фото профиля данного пользователя, чата или канала;
# client.download_file(entity) - низкоуровневый метод загрузки файлов из их исходного местоположения;
# client.iter_download(entity) - итерирует загрузку файла, получая фрагменты файла.
#
# #DIALOGS
# client.iter_dialogs(entity) - итератор над диалогами (открытые разговоры/подписанные каналы);
# client.get_dialogs(entity) - то же , что и  iter_dialogs(), но вместо этого возвращает TotalList;
# client.edit_folder(entity) - редактирует папку, используемую одним или несколькими диалоговыми окнами для их архивирования;
# client.iter_drafts(entity) - итератор над черновиками сообщений;
# client.get_drafts(entity) - то же , что и iter_drafts(), но вместо этого возвращает список;
# client.delete_dialog(entity) - удаляет диалог (покидает чат или канал);
# client.conversation(entity) -создает объект Conversationс заданным объектом.
#
# #USERS
# client.get_me(entity) - получает «О себе», текущего пользователя, вошедшего в систему;
# client.is_bot(entity) - возврат True, если вошедший пользователь является ботом, False в противном случае;
# client.is_user_authorized(entity) - возвращает True, если пользователь авторизован (вошел в систему);
# client.get_entity(entity) - превращает данный объект в допустимого пользователя(entity) Telegram , чат или канал;
# client.get_input_entity(entity)- превращает данный объект в версию входного объекта;
# client.get_peer_id(entity) - получает идентификатор для данной сущности.
#
# #CHATS
# client.iter_participants(entity) - итератор по участникам, принадлежащим указанному чату;
# client.get_participants(entity) - то же , что и iter_participants(), но вместо этого возвращает TotalList;
# client.kick_participant(entity) - выкидывает пользователя из чата;
# client.iter_admin_log(entity) - итератор над журналом администратора для указанного канала;
# client.get_admin_log(entity) - то же , что иiter_admin_log() но вместо этого возвращает list;
# client.iter_profile_photos(entity) - итератор по фотографиям профиля пользователя или фотографиям чата;
# client.get_profile_photos(entity) - то же , что иiter_profile_photos(), но вместо этого возвращает TotalList;
# client.edit_admin(entity) - редактирует права администратора для кого-либо в чате;
# client.edit_permissions(entity) - редактирует ограничения пользователя в чате;
# client.get_permissions(entity) - извлекает разрешения пользователя в определенном чате или канале или получает ограниченные права по умолчанию для чата или канала;
# client.get_stats(entity) - извлекает статистику из заданной мегагруппы или широковещательного канала;
# client.action(entity) - возвращает объект диспетчера контекста для представления «действия чата».