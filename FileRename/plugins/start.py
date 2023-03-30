from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
import random
from FileRename.helper.txt import HELP_TXT, ABOUT_TXT
from FileRename.helper.database import db
from config import FLOOD, ADMIN 


@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id)             
    txt=f"👋 Hai {user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝!"
    button=InlineKeyboardMarkup([[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ-ᴄʜᴀɴɴᴇʟ", callback_data='dev')
        ],[        
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://t.me/TeleBotsUpdate'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/TeleBotxSupport')
        ]])
    if START_PIC:
        await message.reply_photo(START_PIC, caption=txt, reply_markup=button)       
    else:
        await message.reply_text(text=txt, reply_markup=button, disable_web_page_preview=True)
    

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
        await query.message.edit_text(
            text=f"""👋 Hai {query.from_user.mention} \n𝙸'𝚖 𝙰 𝚂𝚒𝚖𝚙𝚕𝚎 𝙵𝚒𝚕𝚎 𝚁𝚎𝚗𝚊𝚖𝚎+𝙵𝚒𝚕𝚎 𝚃𝚘 𝚅𝚒𝚍𝚎𝚘 𝙲𝚘𝚟𝚎𝚛𝚝𝚎𝚛 𝙱𝙾𝚃 𝚆𝚒𝚝𝚑 𝙿𝚎𝚛𝚖𝚊𝚗𝚎𝚗𝚝 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 & 𝙲𝚞𝚜𝚝𝚘𝚖 𝙲𝚊𝚙𝚝𝚒𝚘𝚗 𝚂𝚞𝚙𝚙𝚘𝚛𝚝! """,
            reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help')
        ],[
        InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ-ᴄʜᴀɴɴᴇʟ", callback_data='dev')
        ],[        
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://t.me/TeleBotsUpdate'),
        InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ', url='https://t.me/TeleBotxSupport')
        ]]),)

    elif data == "help":
        await query.message.edit_text(
            text=HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔐 ᴄʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◁ ʙᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(client.mention),
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





