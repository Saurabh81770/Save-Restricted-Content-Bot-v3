# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, STRING
from pyrogram import Client
import sys
import asyncio

# Clients initialize karein
client = TelegramClient("telethonbot", API_ID, API_HASH)
app = Client("pyrogrambot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
userbot = None

if STRING:
    userbot = Client("4gbbot", api_id=API_ID, api_hash=API_HASH, session_string=STRING)

async def start_client():
    try:
        if not client.is_connected():
            await client.start(bot_token=BOT_TOKEN)
            print("Telethon client started...")
        
        if STRING and userbot:
            try:
                await userbot.start()
                print("Userbot started...")
            except Exception as e:
                print(f"Userbot error: {e}")
                # Userbot error se entire app bandh nahi karein
        
        await app.start()
        print("Pyrogram bot started...")
        return client, app, userbot
        
    except Exception as e:
        print(f"Client startup error: {e}")
        sys.exit(1)
