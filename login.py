from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Get Session key
with TelegramClient(StringSession(), '****', '****'+7) as client: #Your API_ID and API_hash
    print(client.session.save())