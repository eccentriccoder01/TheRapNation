import requests
import random
from TheRapNation import app, userbot
from TheRapNation.misc import SUDOERS
from pyrogram import filters, Client
from pyrogram.types import *
from TheRapNation.utils.branded_ban import admin_filter


branded_text = [
    "Hey, please don't disturb me!",
    "Who are you?",
    "Aap kaun ho?",
    "Aap mere Owner to nhi lgte...",
    "Hey, tum mera name kyu le rhe ho merko sone do...",
    "Ha bolo kya kaam hai!",
    "Dekho, abhi mai busy hu!",
    "Hey, I'm busy!",
    "Aapko samajh nhi aata kya?!",
    "Leave me alone!",
    "Dude! What has happened??",
]

strict_txt = [
    "I can't restrict my besties!",
    "Are you serious? I can't restrict my friends!",
    "SHUT THE HELL UP, mai apne dosto ko kyu kru!",
    "Hey, stupid admin!",
    "Ha ye pehele krlo, maar lo ek dusre ke takle par!",
    "I can't, the user is my close friend...",
    "I love this user, please don't restrict this user, try to understand...",
]


ban = ["ban", "boom"]
unban = [
    "unban",
]
mute = ["mute", "silent", "shut"]
unmute = ["unmute", "speak", "free"]
kick = ["kick", "out", "nikaal", "nikal"]
promote = ["promote", "adminship"]
demote = ["demote", "lelo"]
group = ["group"]
channel = ["channel"]


# ========================================= #


@Client.on_message(filters.command(["ip", "iyush"], prefixes=["B", "L"]) & admin_filter)
async def restriction_app(client: Client, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(branded_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")

    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                else:
                    await client.ban_chat_member(chat_id, user_id)
                    await message.reply(
                        "OK, I've banned this Dumb Alien!"
                    )

        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await client.unban_chat_member(chat_id, user_id)
                await message.reply(f"Ok, aap bolte hai to unban kar diya!")

        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))

                else:
                    await client.ban_chat_member(chat_id, user_id)
                    await client.unban_chat_member(chat_id, user_id)
                    await message.reply("Get lost! Bhaga diya gadhe ko...")

        for muted in data:
            print(f"present {muted}")
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))

                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"Muted successfully! Disgusting people...")

        for unmuted in data:
            print(f"present {unmuted}")
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"Huh, OK, Sir!")

        for promoted in data:
            print(f"present {promoted}")
            if promoted in promote:
                await client.promote_chat_member(
                    chat_id,
                    user_id,
                    privileges=ChatPrivileges(
                        can_change_info=False,
                        can_invite_users=True,
                        can_delete_messages=True,
                        can_restrict_members=False,
                        can_pin_messages=True,
                        can_promote_members=False,
                        can_manage_chat=True,
                        can_manage_video_chats=True,
                    ),
                )
                await message.reply("Promoted!")

        for demoted in data:
            print(f"present {demoted}")
            if demoted in demote:
                await client.promote_chat_member(
                    chat_id,
                    user_id,
                    privileges=ChatPrivileges(
                        can_change_info=False,
                        can_invite_users=False,
                        can_delete_messages=False,
                        can_restrict_members=False,
                        can_pin_messages=False,
                        can_promote_members=False,
                        can_manage_chat=False,
                        can_manage_video_chats=False,
                    ),
                )
                await message.reply("Demoted!")
