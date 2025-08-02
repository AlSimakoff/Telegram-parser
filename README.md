📡 Telegram Message Forwarder Bot

Этот бот на базе библиотеки Telethon автоматически пересылает сообщения и альбомы (группы фотографий) из указанных Telegram-каналов в целевой чат, с фильтрацией дубликатов и "паст" (очень похожих сообщений).
⚙️ Функциональность

    🔁 Пересылка новых сообщений и альбомов из заданных каналов.

    📸 Поддержка фотоальбомов.

    🧠 Алгоритм обнаружения похожих сообщений ("паст") на основе difflib.

    ❌ Не пересылает сообщения, уже отправленные ранее (по ID).

    ⏱ Асинхронная работа через Telethon.

📦 Установка

    Установи зависимости:

pip install telethon

    Получи свои API_ID и API_HASH:
    Зарегистрируйся на my.telegram.org → API Development Tools.

🧠 Использование

    Сначала сгенерируй строку сессии:

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())

    Вставь полученную строку сессии в основной скрипт (SESSION_STRING).

    Запусти основной файл:

python main.py

📝 Конфигурация

В коде задаются источники сообщений:

channel1 = '@Kecsik'
channel2 = client.get_entity('https://t.me/dvachannel')
channel3 = client.get_entity('https://t.me/breakingmash')
...
source_channel = [channel1, channel2, ...]

И канал/чат-получатель:

channel = types.PeerChat(890823314)  # Замените на ваш ID или используйте get_entity

    💡 ID чата можно получить с помощью client.get_entity(...).

🚫 Фильтрация "паст"

Используется библиотека difflib, чтобы определить, насколько текущее сообщение похоже на одно из предыдущих (порог — 75%). Если похоже, сообщение не пересылается.
🧵 Пример логов

script is run
foto in album 0
pasta - 0.80
message from album or message is pasta

🛡 Предупреждение

    Убедись, что у бота есть права на чтение в каналах и отправку в целевой чат.

    Использование публичных каналов требует авторизации и может нарушать ToS Telegram.

📃 Лицензия

MIT License
