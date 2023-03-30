from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from FileRename.helper.txt import mr
from FileRename.helper.database import db
from config import FLOOD, ADMIN 



START_IMG = "https://graph.org/file/8665aaff4579f6734a730.jpg"

START_TXT = f"""
ʜᴇʟʟᴏ {user.mention}
ɪ ᴀᴍ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ʙᴏᴛ 
ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ"
    
"""


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ-ᴄʜᴀɴɴᴇʟ", url='https://youtube.com/@AsTechnical.')
        ],[        
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://t.me/TeleBotsUpdate'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/TeleBotxSupport')
        ]])
    await message.reply_photo((START_IMG), caption=(START_TXT), reply_markup=button)       
    

@Client.on_message(filters.command('logs') & filters.user(ADMIN))
async def log_file(client, message):
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply_text(f"ᴇʀʀᴏʀ:\n`{e}`")

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ.**\n\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 sᴛᴀʀᴛ ʀᴇɴᴀᴍᴇ 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.value)
        text = f"""**ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ғɪʟᴇ**\n\n**ғɪʟᴇ ɴᴀᴍᴇ** :- `{filename}`\n\n**ғɪʟᴇ sɪᴢᴇ** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 sᴛᴀʀᴛ ʀᴇɴᴀᴍᴇ 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(text=(START_TXT),
           reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ-ᴄʜᴀɴɴᴇʟ", url='https://youtube.com/@AsTechnical.')
        ],[        
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://t.me/TeleBotsUpdate'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/TeleBotxSupport')
        ]]),)
          

    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔐 ᴄʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◁ ʙᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
               InlineKeyboardButton("🔐 ᴄʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◁ ʙᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





