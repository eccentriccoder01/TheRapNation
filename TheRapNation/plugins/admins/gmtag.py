from TheRapNation import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [
 " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌚** ",
 " **➠ ᴄʜᴜᴘ ᴄʜᴀᴘ sᴏ ᴊᴀ 🙊** ",
 " **➠ ᴘʜᴏɴᴇ ʀᴀᴋʜ ᴋᴀʀ sᴏ ᴊᴀ, ɴᴀʜɪ ᴛᴏ ʙʜᴏᴏᴛ ᴀᴀ ᴊᴀʏᴇɢᴀ..👻** ",
 " **➠ ᴋᴀʟ ᴄʜᴜᴛᴛɪ ɴᴀʜɪ ʜ ʙʜᴀɪ, ᴀʙʜɪ sᴏ ᴊᴀᴏ 💤** ",
 " **➠ ʀᴀᴊᴀɪ ᴍᴇɪɴ ɢʜᴜs ᴋᴀʀ ғᴏɴ ᴄʜᴀʟᴀ ʀʜᴀ ʜ, ᴍᴜᴍᴍʏ ᴅᴇᴋʜ ʟᴇɴɢɪ 😜** ",
 " **➠ ᴘᴀᴘᴀ ʏᴇ ʙᴇᴛᴀ ᴀʙʜɪ ᴛᴀᴋ ᴘʜᴏɴᴇ ᴄʜᴀʟᴀ ʀʜᴀ ʜᴀɪ 🤭** ",
 " **➠ ʙʀᴏ ʀᴀᴀᴛ ᴋᴀ ᴄʜɪʟʟ sᴇssɪᴏɴ ʜᴏɢᴀ? 🌠** ",
 " **➠ ɢɴ sᴅ ᴛᴄ.. 🙂** ",
 " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ, sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ʙʀᴏ ✨** ",
 " **➠ ʀᴀᴀᴛ ʙʜᴜᴛ ʜᴏ ɢʏɪ ʜᴀɪ, sᴏ ᴊᴀᴏ 🌌** ",
 " **➠ 11 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ, ᴀʙʜɪ ᴛᴀᴋ ʜᴀᴛʜ ᴍᴇɪɴ ғᴏɴ, ᴍᴜᴍᴍʏ ᴅᴇᴋʜ ʟᴇɴɢɪ 🕦** ",
 " **➠ sᴄʜᴏᴏʟ ɴᴀʜɪ ᴊᴀɴᴀ ᴋʏᴀ ᴋᴀʟ, ʙʀᴏ 😤** ",
 " **➠ ʙʀᴏ ɢɴ sᴅ ᴛᴄ 😊** ",
 " **➠ ᴀᴀᴊ ʙʜᴜᴛ ᴛʜᴀɴᴅ ʜᴀɪ, ʀᴀᴊᴀɪ ᴍᴇɪɴ ɢʜᴜs ᴋᴀʀ ʙᴀɴᴅᴀ ʙᴀɴ ᴊᴀ 🌼** ",
 " **➠ ʙʀᴏ ɢɴ 🌷** ",
 " **➠ ᴍᴀɪɴ ʙʜɪ ɴɪᴋʟʀᴀ ʜᴜ, ɢɴ 🏵️** ",
 " **➠ ɴᴀᴍᴀsᴛᴇ, ᴄʜᴇᴄᴋɪɴɢ ᴏᴜᴛ ғᴏʀ ᴛʜᴇ ᴅᴀʏ 🍃** ",
 " **➠ ʙʜᴀɪ ᴀʙʜɪ ᴛᴀᴋ ᴊᴀɢ ʀʜᴇ ʜᴏ, ᴋᴀʀᴋᴇ ᴋʏᴀ ʀᴀᴍ ɴᴀᴍ? ☃️** ",
 " **➠ ʙʜᴜᴛ ʀᴀᴀᴛ ʜᴏ ɢʏɪ, ɢɴ ⛄** ",
 " **➠ ʀᴏɴᴀ ɴᴀʜɪ, sᴏɴᴀ ʜᴀɪ 😁** ",
 " **➠ ғɪsʜ ᴍᴀᴛ ʜᴏ ʙʜᴀɪ, ᴋᴀʟ ᴋᴀᴍ ʜᴀɪ, sᴏ ᴊᴀ 🌄** ",
 " **➠ ɢɴ ʙʀɪɢʜᴛғᴜʟʟ ɴɪɢʜᴛ 🤭** ",
 " **➠ ɴɪɢʜᴛ ғᴏʀ ᴛʜᴇ ʙᴇᴀsᴛs ᴛᴏ ʀᴇsᴛ 😎** ",
 " **➠ ᴅʀᴇᴀᴍ ʙɪɢ, sʟᴇᴇᴘ ʜᴀʀᴅ ❤️** ",
 " **➠ ɢɴ, ᴅᴏɴ'ᴛ ʟᴇᴛ ᴛʜᴇ ᴅʀᴇᴀᴍs ʙɪᴛᴇ 💚** ",
 " **➠ ɢɴ ʙʜᴀɪ, ɴɪɴᴅ ᴀʀʜɪ 🥱** ",
 " **➠ ɢɴ ғʀɪᴇɴᴅ 💤** ",
 " **➠ ʙʜᴀɪ ᴀᴊ ᴋᴜᴄʜ ᴘʟᴀɴ ʜᴀɪ ᴋʏᴀ 😏** ",
 " **➠ ʀᴀᴀᴛ ᴍᴇɪɴ ᴊᴀɢ ᴋᴇ ᴋʏᴀ ᴄʜᴀɴᴅ ʙᴀɴᴇɢᴀ? 😜** ",
 " **➠ ᴄʟᴏsᴇ ʏᴏᴜʀ ᴇʏᴇs, ʀᴇsᴛ ʏᴏᴜʀ ɢʀɪᴘ,, ᴋᴀʟ ᴘɪᴛᴀʏɪ ʜᴀɪ ᴋᴀᴍ ᴍᴇɪɴ 💫** ",
]

VC_TAG = [
 "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴋᴀɪsᴀ ʜᴀɪ ʙʀᴏ 🐱**",
 "**➠ ᴜᴛʜɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 🌤️**",
 "**➠ ɢᴍ ʙʀᴏ, ᴄʜᴀɪ ʙᴀɴ ᴄʜᴜᴋɪ ☕**",
 "**➠ ᴜᴛʜᴏ ʙʀᴏ, sᴄʜᴏᴏʟ ʜᴀɪ ɴᴀ 🏫**",
 "**➠ ᴄʜᴜᴘ ᴄʜᴀᴘ ʙɪsᴛʀᴀ ᴄʜᴏʀ ɴᴀʜɪ ᴛᴏ ᴘᴀɴɪ ᴀᴀʏᴇɢᴀ 🧊**",
 "**➠ ᴜᴛʜ ᴊᴀ ᴏʀ ғʀᴇsʜ ʜᴏ, ʙʀᴇᴀᴋғᴀsᴛ ʟᴀɢɪ ʜᴀɪ 🫕**",
 "**➠ ᴏғғɪᴄᴇ ʙᴀɴᴅ ɴᴀʜɪ ʜᴀɪ, ʙʜᴀɪ ᴜᴛʜ ᴊᴀᴏ 🏣**",
 "**➠ ɢᴍ ᴅᴏsᴛ, ᴄʜᴀɪ ʏᴀ ᴄᴏғғᴇᴇ? ☕🍵**",
 "**➠ ʙʜᴀɪ 8 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ, ᴜᴛʜ ᴊᴀ 🕖**",
 "**➠ ᴋʜᴜᴍʙʜᴋᴀʀᴀɴ ᴋɪ ᴊᴀᴀᴛ ᴜᴛʜ ᴊᴀ ☃️**",
 "**➠ ɢᴍ, ɴɪᴄᴇ ᴅᴀʏ ʙʜᴀɪ 🌄**",
 "**➠ ᴅᴀʏ sᴛᴀʀᴛᴇᴅ, ʙʜᴀɪ ᴄʜᴀʀɢᴇ ʟᴇʟᴏ 🪴**",
 "**➠ ɢᴍ ʙʀᴏ, ᴀʟʟ sᴇᴛ ғᴏʀ ᴛʜᴇ ᴅᴀʏ 😇**",
 "**➠ ᴍᴜᴍᴍʏ ᴋᴏ ʙᴏʟᴏ ʏᴇ ʙᴀʟᴀᴋ ᴀʙʜɪ ᴛᴀᴋ sᴏ ʀʜᴀ 😵‍💫**",
 "**➠ ʀᴀᴀᴛ ʙʜᴀʀ ᴄʜɪʟʟ ᴋʀɴᴇ ᴋᴇ ʙᴀᴀᴅ, ᴜᴛʜɴᴀ ᴘᴀᴅᴇɢᴀ 😏**",
 "**➠ ɢᴍ ʙʜᴀɪ, ғʀɪᴇɴᴅs ᴋᴏ ᴡɪsʜ ᴋᴀʀᴅᴇ 🌟**",
 "**➠ ᴘᴀᴘᴀ ʙᴏʟ ʀʜᴇ, ᴜᴛʜɴᴀ ʜᴀɪ ʙᴇᴛᴀ 🥲**",
 "**➠ ʙʀᴏ, ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ.. ᴋᴀʀ ᴋʏᴀ ʀʜᴇ ʜᴏ 😅**",
 "**➠ ɢᴍ ʙᴇsᴛɪᴇ, ʙʀᴇᴀᴋғᴀsᴛ ʜᴜᴀ ᴋɪ ɴᴀʜɪ? 🍳**",
]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ᴅᴇᴀʀ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ᴅᴇᴀʀ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ᴅᴇᴀʀ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ᴅᴇᴀʀ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")
