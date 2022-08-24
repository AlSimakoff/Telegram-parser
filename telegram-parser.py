from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events, types, utils
import logging
import asyncio

API_ID = **** #Your API_ID
API_HASH = **** #Your API_Hash
SESSION_STRING = '****' #Your Session Key

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
client.start()

# target channel
channel = types.PeerChannel(1652645965)

channel1 = client.get_entity('https://t.me/wargonzo')
channel2 = client.get_entity('https://t.me/dvachannel')
channel3 = client.get_entity('https://t.me/breakingmash')
channel4 = client.get_entity('https://t.me/ru2ch_news')
channel5 = client.get_entity('https://t.me/nrpublic')
channel6 = client.get_entity('https://t.me/joinchat/AAAAAEZpXWl_yw-M6mrz5w')
channel7 = client.get_entity('https://t.me/Cbpub')
source_channel = [channel1, channel2, channel3,
                  channel4, channel5, channel6, channel7]

id=[]
@client.on(events.Album(chats=(source_channel)))
async def handler(event):
    global id
    id=[]
    for i in range(len(event.messages)):
        id.append(event.messages[i].id)
    await client.send_file(channel, file=event.messages, caption=event.text)

@client.on(events.NewMessage(chats=(source_channel)))
async def normal_handler(event):
    await asyncio.sleep(3)
    global id
    if event.message.id in id:
        print('message from album', event.message.id)
    else:
        await client.send_message(channel, event.message)

print('script is run')

client.start()

client.run_until_disconnected()




