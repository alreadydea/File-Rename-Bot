import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from random import choice
from config import API_ID, API_HASH, BOT_TOKEN 
from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command("clone"))
async def clone(bot, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴀɢᴇ:\n\n/clone ʏᴏᴜʀ_ʙᴏᴛ_ᴛᴏᴋᴇɴ")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("<code>ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...</code>")                   
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "FileRename.plugins"})
        await client.start()
        user = await client.get_me()
        await msg.reply(f"ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ʜᴀs ʙᴇᴇɴ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ᴀs @{user.username}! ✅ \n\n ɴᴏᴡ ʏᴏᴜʀ ʙᴏᴛ ʜᴏsᴛᴇᴅ ɪɴ ᴍʏ ʙᴏᴛ sᴇʀᴠᴇʀ\n\nᴛʜᴀɴᴋs ғᴏʀ ᴄʟᴏɴɪɴɢ.")
    except Exception as e:
        await msg.reply(f"**ᴇʀʀᴏʀ:** `{str(e)}`\nᴘʀᴇss /start ᴛᴏ sᴛᴀʀᴛ ᴀɢᴀɪɴ.")
