from ast import For
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient, events
from time import sleep
import logging;
from telethon import types, utils
import asyncio
import difflib

API_ID = '14260225'
API_HASH = '587676597964ac0bbf1fc20a243877be'
SESSION_STRING = '1ApWapzMBu7pws3MmsyrTwbLMoHFsvheT1CoTWXTmifHBbs6X4du1Xf_38_Kl1IPYKIUbxgzoFOlHzStk7cJjMQb6e_50BdYmusT4HKn1PKlg26JOgTPdmYVl9EECgmN5SuvtlWGdn41FAuuNAP_QkNl_5sqYn41tPqySN_iPvjNuIf_I2530q8ffbHct6vFOYxtkdS8eNUg_efgS6AHQKWKOkCYR5iRhCMyJ2sy6CktOHJPv-kGsmVy3RHfElnjIEA662ADOhqSIK9DbSg-Dl9fxcc_BmbwpoFf_KwTVGDCUJhAM67dSVuVP6m9YDlimwMAVFpZ3_qmlYoGhIN2KsPIj9AF4ZLU='
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

client.start()

channel = types.PeerChat(890823314)

channel1 = '@Kecsik'
channel2 = client.get_entity('https://t.me/dvachannel')
channel3 = client.get_entity('https://t.me/breakingmash')
channel4 = client.get_entity('https://t.me/ru2ch_news')
channel5 = client.get_entity('https://t.me/nrpublic')
channel6 = client.get_entity('https://t.me/joinchat/AAAAAEZpXWl_yw-M6mrz5w')
channel7 = client.get_entity('https://t.me/Cbpub')
source_channel = [channel1, channel2, channel3,
                  channel4, channel5, channel6, channel7]

id=[]
msg_arh=[]


s1 = "текст1"
s2 = "текст2"

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()
  


@client.on(events.Album(chats=(source_channel)))
async def handler(event):
    global id
    id=[]
    for i in range(len(event.messages)):
        id.append(event.messages[i].id)
        print('foto in album', i)
    await client.send_file(channel, file=event.messages, caption=event.text)

@client.on(events.NewMessage(chats=(source_channel)))
async def normal_handler(event):
    await asyncio.sleep(3)
    global id
    global msg_arh
    pasta=False
    print()
    for i in range(len(msg_arh)):
        cpypste=similarity(msg_arh[i], event.message.message)
        if cpypste>0.75:
            pasta=True
        print('pasta -', cpypste)
    msg_arh.append(event.message.message)

    if len(msg_arh)>20:
        del msg_arh[0]
    if event.message.id in id or pasta==True:
        print('message from album or message is pasta')
    else:
        await client.send_message(channel, event.message)

print('script is run')

client.start()

client.run_until_disconnected()


