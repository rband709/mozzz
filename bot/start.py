
import os
import logging
import ffmpeg
import asyncio
import json
import requests
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "Shazam",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


START_TEXT = """Hello {}
I am Shazam Music Search bot. \
Send me audio file for search result.
> `I can search in inline too. [Coming Soon]`
Made by @TheTeleRoid"""

JOIN_BUTTON = [
    InlineKeyboardButton(
        text='⭕ Updates Channel ⭕',
        url='https://telegram.me/TeleRoidGroup'
    )
]


@bot.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply_text(
        text=START_TEXT.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([JOIN_BUTTON]),
        disable_web_page_preview=True,
        quote=True
    )
       
bot.start()
idle()    
