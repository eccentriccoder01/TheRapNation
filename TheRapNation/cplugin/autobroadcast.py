import asyncio
import datetime
from pyrogram import Client
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from typing import Dict, List, Union
from TheRapNation.utils.database import get_served_chats_clone
from TheRapNation import userbot
from TheRapNation.core.mongo import mongodb, pymongodb

AUTO_GCAST = True

START_IMG_URLS = "https://i.pinimg.com/1200x/fd/8c/88/fd8c888ec4d2a4a5ebad3f6257084792.jpg"

MESSAGES = f"""**✅

**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ BRAND ๏",
                url=f"https://t.me/the_rap_nation",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟʏʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/the_rap_nationBot?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @TheRapNationBot"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/the_rap_nationBot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""


async def send_message_to_chats(client: Client):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(
                        1
                    )  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_cbroadcast():
    # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats(client)
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(5)


# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:
    asyncio.create_task(continuous_cbroadcast())
