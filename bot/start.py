"""
    Shazam Telegram Bot
    Copyright (C) 2021 @PredatorHackerzZ
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os
import logging
import ffmpeg
import asyncio
import json
import requests
from ShazamAPI import Shazam
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
