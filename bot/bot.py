import os
import logging
import ffmpeg
import asyncio
import json
import requests
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import API_ID, API_HASH, BOT_TOKEN
from configparser import ConfigParser
from shazamio import Shazam, exceptions, FactoryArtist, FactoryTrack

shazam = Shazam()


class bot(Client):
    def __init__(self, name):
        config = ConfigParser()
        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=16,
            workdir="./",
        )

    async def start(self):
        await super().start()
        print("bot started. Hi.")

    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")

    async def recognize(self, path):
        return await shazam.recognize_song(path)

    async def related(self, track_id):
        try:
            return (await shazam.related_tracks(track_id=track_id, limit=50, start_from=2))['tracks']
        except exceptions.FailedDecodeJson:
            return None
    
    async def get_artist(self, query: str):
        artists = await shazam.search_artist(query=query, limit=50)
        hits = []
        try:
            for artist in artists['artists']['hits']:
                hits.append(FactoryArtist(artist).serializer())
            return hits
        except KeyError:
            return None
        
    async def get_artist_tracks(self, artist_id: int):
        tracks = []
        tem = (await shazam.artist_top_tracks(artist_id=artist_id, limit=50))['tracks']
        try:
            for track in tem:
                tracks.append(FactoryTrack(data=track).serializer())
            return tracks
        except KeyError:
            return None
bot.run
