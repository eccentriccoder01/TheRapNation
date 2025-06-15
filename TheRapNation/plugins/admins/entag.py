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
    " **※ ɪ ᴅᴏɴ'ᴛ ᴏᴡᴇ ʏᴏᴜ sʜɪᴛ...ᰔᩚ**",
    " **※ ғᴏʀɢᴇᴛ ᴀʙᴏᴜᴛ ᴍᴇ ʟɪᴋᴇ ʏᴏᴜ ᴅɪᴅ ʏᴏᴜʀ ɢʏᴍ ʀᴏᴜᴛɪɴᴇ...ᰔᩚ**",
    " **※ ɴᴏ ʟᴏᴠᴇ ʟᴇғᴛ, ᴏɴʟʏ ᴍᴇᴍᴇs...ᰔᩚ**",
    " **※ ᴛʜɪs ɢʀᴏᴜᴘ ɴᴇᴇᴅs ᴍᴇ ᴍᴏʀᴇ ᴛʜᴀɴ ʏᴏᴜ ᴅᴏ...ᰔᩚ**",
    " **※ ɴᴀᴍᴇ ɪɴ ʜᴇᴀʀᴛ? ɴᴀʜ, ɪᴛ's ɪɴ ᴍʏ ᴘᴀʏʟᴀᴛᴇʀ ʟɪsᴛ...ᰔᩚ**",
    " **※ ʏᴏᴜʀ ғʀɪᴇɴᴅs? ᴘʀᴏʙᴀʙʟʏ ɪɴ ᴍʏ ᴅᴍs...ᰔᩚ**",
    " **※ ᴍᴇᴍᴏʀɪᴇs? ɪ ᴏɴʟʏ ʀᴇᴍᴇᴍʙᴇʀ ᴘᴀssᴡᴏʀᴅs...ᰔᩚ**",
    " **※ ᴘʀᴏғᴇssɪᴏɴ: ғᴜʟʟ-ᴛɪᴍᴇ ᴘʀᴏʙʟᴇᴍ...ᰔᩚ**",
    " **※ ʟɪᴠɪɴɢ ɪɴ ʏᴏᴜʀ ʜᴇᴀᴅ ʀᴇɴᴛ ғʀᴇᴇ...ᰔᩚ**",
    " **※ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʙᴜɪʟᴅ ᴅɪғғᴇʀᴇɴᴛ...ᰔᩚ**",
    " **※ ɢᴏᴏᴅ ɴɪɢʜᴛ. ʀᴇsᴛ ɪs ᴄᴏɴsɪsᴛᴇɴᴄʏ...ᰔᩚ**",
    " **※ ғᴇᴇʟɪɴɢ ʙʀᴏᴋᴇʀ ᴛʜᴀɴ ᴍʏ ᴡɪғɪ...ᰔᩚ**",
    " **※ sᴏᴍᴇᴏɴᴇ sᴀʏ ʜɪ ʙᴇғᴏʀᴇ ɪ ᴛᴀʟᴋ ᴛᴏ ᴍʏsᴇʟғ...ᰔᩚ**",
    " **※ ᴡʜᴀᴛ’s ғᴏʀ ᴅɪɴɴᴇʀ? ʜᴏᴘᴇғᴜʟʟʏ ᴇᴅɪʙʟᴇ...ᰔᩚ**",
    " **※ ɪs ᴛʜɪs ʀᴇᴀʟ ʟɪғᴇ ᴏʀ ᴀɴᴏᴛʜᴇʀ ᴢᴏᴏᴍ ᴄᴀʟʟ...ᰔᩚ**",
    " **※ ᴡʜʏ ᴅᴏɴ'ᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ? ʟᴏsᴛ ʏᴏᴜʀ ғɪɴɢᴇʀs?...ᰔᩚ**",
    " **※ ɪ’ᴍ ɪɴɴᴏᴄᴇɴᴛ ᴜɴᴛɪʟ ᴘʀᴏᴠᴇɴ ᴏᴘ...ᰔᩚ**",
    " **※ ʏᴇsᴛᴇʀᴅᴀʏ ᴡᴀs ғɪʀᴇ, ɴᴏ ᴄᴀᴘ...ᰔᩚ**",
    " **※ ᴡᴀs ɢʀɪɴᴅɪɴɢ ʏᴇsᴛᴇʀᴅᴀʏ, ʏᴏᴜ?...ᰔᩚ**",
    " **※ ᴛʜɪs ɢʀᴏᴜᴘ ɴᴇᴇᴅs ᴍᴏʀᴇ ᴘᴏᴡᴇʀ ғʀɪᴇɴᴅs...ᰔᩚ**",
    " **※ ᴄᴀɴ ʏᴏᴜ sɪɴɢ? ɪ ᴄᴀɴ ʙᴀʀᴋ...ᰔᩚ**",
    " **※ ʟᴇᴛ’s ᴛᴀᴋᴇ ᴀ ᴡᴀʟᴋ ᴛᴏ ᴛʜᴇ ғʀɪᴅɢᴇ...ᰔᩚ**",
    " **※ sᴛᴀʏ sᴏʟɪᴅ, ᴀʟᴡᴀʏs...ᰔᩚ**",
    " **※ ғʀɪᴇɴᴅs? ʏᴇᴀʜ ʟɪᴋᴇ ᴛᴇᴀᴍ ᴅᴏᴇᴍ...ᰔᩚ**",
    " **※ ᴍᴀʀʀɪᴇᴅ ᴛᴏ ᴛʜᴇ ɢʀɪɴᴅ...ᰔᩚ**",
    " **※ ɢʜᴏsᴛ ᴍᴏᴅᴇ ғᴏʀ ᴀ ғᴇᴡ ᴅᴀʏs...ᰔᩚ**",
    " **※ ʟɪɴᴋ ɪɴ ʙɪᴏ. ʙʀɪɴɢ ᴀ sɴᴀᴄᴋ...ᰔᩚ**",
    " **※ ᴡᴀs ғᴜɴ, ᴜɴᴛɪʟ ᴛʜᴇ ᴡɪғɪ ᴅɪᴇᴅ...ᰔᩚ**",
    " **※ ɢʀᴏᴜᴘ ᴏᴡɴᴇʀ? ɴᴏ, ᴊᴜsᴛ ᴛʜᴇ ᴍᴇᴍᴇ ᴅᴇᴀʟᴇʀ...ᰔᩚ**",
    " **※ ɴᴏsᴛᴀʟɢɪᴀ ʜɪᴛs ʜᴀʀᴅ ʟᴀᴛᴇ ɴɪɢʜᴛ...ᰔᩚ**",
    " **※ ʟᴇᴛ’s ᴘᴀʀᴛʏ ʟɪᴋᴇ ᴛʜᴇ ᴄᴏᴅᴇ ᴄᴏᴍᴘɪʟᴇᴅ...ᰔᩚ**",
    " **※ ᴡʜᴀᴛ ᴠɪʙᴇs ᴛᴏᴅᴀʏ?...ᰔᩚ**",
    " **※ ʟɪsᴛᴇɴ ᴜᴘ, ɪᴛ’s ɪᴍᴘᴏʀᴛᴀɴᴛ... ᴋɪɴᴅᴀ...ᰔᩚ**",
    " **※ ᴡʜᴀᴛ ᴅɪᴅ ʏᴏᴜ ᴅᴏ ᴛᴏᴅᴀʏ, ᴋɪɴɢ?...ᰔᩚ**",
    " **※ sᴀᴡ ʏᴏᴜ ɢᴏ ᴏғғʟɪɴᴇ, ᴛᴏᴏ ʙᴀᴅ...ᰔᩚ**",
    " **※ ᴀᴅᴍɪɴ? ɴᴀʜ, ᴊᴜsᴛ ᴛʜᴇ ʜᴜᴍᴀɴ ɢʟɪᴛᴄʜ...ᰔᩚ**",
    " **※ ɴᴏ ᴄᴏᴍᴍɪᴛᴍᴇɴᴛs, ᴏɴʟʏ ᴄᴏᴏᴋɪᴇs...ᰔᩚ**",
    " **※ ᴘʀɪsᴏɴᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀᴛ ʟᴏᴏᴘ...ᰔᩚ**",
    " **※ sᴀᴡ ʏᴏᴜ ʏᴇsᴛᴇʀᴅᴀʏ, sᴄʀᴏʟʟɪɴɢ ʟɪᴋᴇ ᴀ ʙᴏss...ᰔᩚ**",
    " **※ ғʀᴏᴍ ᴛʜᴇ ʟᴀɴᴅ ᴏғ ᴡɪғɪ ᴅʀᴏᴘs...ᰔᩚ**",
    " **※ ᴏɴʟɪɴᴇ, ʙᴜᴛ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ...ᰔᩚ**",
    " **※ ғᴀᴠ ᴇᴀᴛ? ᴀɴʏᴛʜɪɴɢ ᴛʜᴀᴛ’s ғʀᴇᴇ...ᰔᩚ**",
    " **※ ᴀᴅᴅ ᴍᴇ ғᴏʀ ᴍᴜsɪᴄ + ᴍᴇᴍᴇs, ɴᴏ ᴄᴀᴘ...ᰔᩚ**",
    " **※ ᴛʀᴜᴛʜ ᴏʀ ᴅᴀʀᴇ? ɪ ᴅᴀʀᴇ ʏᴏᴜ ᴛᴏ sᴛᴀʏ ᴏғғʟɪɴᴇ...ᰔᩚ**",
    " **※ ʙᴇᴇɴ sᴜs ʟᴀᴛᴇʟʏ, ᴀɪɴ'ᴛ ɢᴏɴɴᴀ ʟɪᴇ...ᰔᩚ**",
    " **※ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴᴇᴅ? ʙᴜғғᴇʀɪɴɢ ʟɪғᴇ...ᰔᩚ**",
    " **※ ᴄʜᴏᴄᴏʟᴀᴛᴇ? ɴᴀʜ, ᴘʀᴏᴛᴇɪɴ ʙᴀʀs...ᰔᩚ**",
    " **※ ʜᴇʏ ᴋɪɴɢ, ᴡᴀᴋᴇ ᴜᴘ...ᰔᩚ**",
    " **※ ʙᴇ ᴍᴀɴ ᴇɴᴏᴜɢʜ ᴛᴏ sᴘᴀᴍ ᴍᴇ ᴛᴏᴏ...ᰔᩚ**",
    " **※ ʏᴏᴜ sᴀʏɪɴ’ ɢᴏᴏᴅ ᴏʀ ɢᴏɴᴇ?...ᰔᩚ**",
    " **※ ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ? ɴᴀʜ, sᴇɴᴅ ᴍᴇ ᴍᴇᴍᴇs ɪɴsᴛᴇᴀᴅ...ᰔᩚ**"
]

VC_TAG = [
    " **※ আমি তোকে কিছুই ধার দিইনি...💥**",
    " **※ যেমন জিম ছেড়েছিস, তেমন আমাকেও ভুলে যা...💥**",
    " **※ ভালোবাসা শেষ, এখন শুধু মিম আছে...💥**",
    " **※ এই গ্রুপ আমাকে বেশি দরকার...💥**",
    " **※ নাম মনে রাখিস না, পেমেন্ট ডিউ মনে রাখ...💥**",
    " **※ তোর বন্ধু? ও তো আমার ইনবক্সে...💥**",
    " **※ স্মৃতি? পাসওয়ার্ড ছাড়া কিছু মনে থাকে না...💥**",
    " **※ প্রফেশন? ফুল-টাইম প্রবলেম...💥**",
    " **※ মাথায় ভাড়া না দিয়ে থাকি...💥**",
    " **※ সুপ্রভাত। বিল্ড ডিফারেন্ট...💥**",
    " **※ শুভরাত্রি। কনসিস্টেন্সিই আসল বিশ্রাম...💥**",
    " **※ আমার অবস্থা এখন WiFi এর চেয়ে খারাপ...💥**",
    " **※ কেউ কথা বলবি? নাহলে নিজেকেই মেসেজ করব...💥**",
    " **※ রাতের খাবারে কি? খাওয়া গেলেই হলো...💥**",
    " **※ এটা লাইফ না, আরেকটা জুম মিটিং মনে হচ্ছে...💥**",
    " **※ মেসেজ করিস না কেন? হাত ভেঙে গেছে নাকি?...💥**",
    " **※ নির্দোষ, যতক্ষণ না প্রমাণ হয় আমি অপ...💥**",
    " **※ গতকাল 🔥 ছিলো, নো ক্যাপ...💥**",
    " **※ কালও গ্রাইন্ড করছিলাম, তুই?...💥**",
    " **※ এই গ্রুপে পাওয়ারফুল বন্ধুর দরকার...💥**",
    " **※ গান গাইতে পারিস? আমি তো ঘেউ ঘেউ করতে পারি...💥**",
    " **※ চল ফ্রিজ পর্যন্ত হাঁটি...💥**",
    " **※ সবসময় স্টেডি থাক...💥**",
    " **※ বন্ধুরা? টিম ডুমের মত...💥**",
    " **※ গ্রাইন্ডের সাথে বিয়ে হয়েছে...💥**",
    " **※ কিছুদিন ঘোস্ট মোডে থাকব...💥**",
    " **※ বায়োতে লিংক দিছি। খাবার নিয়েই আসিস...💥**",
    " **※ মজা হচ্ছিল, WiFi মারা না গেলে ভালোই চলছিল...💥**",
    " **※ আমি গ্রুপের মালিক না, মিম ডিলার...💥**",
    " **※ রাত গভীরে নস্টালজিয়া মেরে দেয়...💥**",
    " **※ পার্টি কর যেন কোড কম্পাইল হয়ে গেছে...💥**",
    " **※ আজকের ভাইব কী?...💥**",
    " **※ শোন, কিছু জরুরি কথা বলার আছে... একটু...💥**",
    " **※ আজ কী করলি, ভাই?...💥**",
    " **※ দেখলাম অফলাইন চলে গেলি...😮‍💨💥**",
    " **※ অ্যাডমিন? না রে, আমি তো হিউম্যান গ্লিচ...💥**",
    " **※ কোনো কমিটমেন্ট না, শুধু কুকি...💥**",
    " **※ এই চ্যাট লুপের বন্দী হয়ে গেছি...💥**",
    " **※ গতকাল তোকে দেখলাম স্ক্রল করতে, বসের মতো...💥**",
    " **※ WiFi-হীন জমির লোক আমি...💥**",
    " **※ অনলাইন আছি, কিন্তু অ্যাভেইলেবল না...💥**",
    " **※ ফেভারিট খাবার? যেটা ফ্রি সেটা...💥**",
    " **※ মিউজিক + মিম চাইলে আমাকে অ্যাড দে, নো ক্যাপ...💥**",
    " **※ ট্রুথ নাকি ডেয়ার? ডেয়ার দিলাম অফলাইনে থাক...💥**",
    " **※ একটু সাস হচ্ছি, বলেই দিলাম...💥**",
    " **※ কী হইল? জীবন বাফারিং করছে...💥**",
    " **※ চকোলেট? না ভাই, প্রোটিন বার...💥**",
    " **※ ওঠ ভাই, দিন শুরু হইছে...💥**",
    " **※ আমাকেও একটু স্প্যাম কর, ভাই হয়ে যা...💥**",
    " **※ বিদায় বললি নাকি আবার সাস করলি?...💥**",
    " **※ WhatsApp নাম্বার না, মিম পাঠা বরং...💥**"
]



@app.on_message(filters.command(["entag", "englishtag" ], prefixes=["/", "@", "#"]))
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
        return await message.reply("/entag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/entag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/entag ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏʀ ᴛᴀɢɢɪɴɢ...")
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


@app.on_message(filters.command(["bntag"], prefixes=["/", "@", "#"]))
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



@app.on_message(filters.command(["cancel", "enstop", "bnstop"]))
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
          
