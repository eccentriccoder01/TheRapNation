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

TAGMES_MASC = [
" **𝐇𝐞𝐲 𝐁𝐡𝐚𝐢 𝐊𝐡𝐚𝐝𝐞 𝐇𝐨 𝐊𝐲𝐚🤗🥱** ",
" **𝐎𝐲𝐞 𝐊𝐡𝐚𝐫𝐞 𝐇𝐨 𝐊𝐲𝐚? 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
" **𝐕𝐂 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐃𝐨𝐬𝐭𝐨𝐧 𝐖𝐚𝐥𝐢😃** ",
" **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐚 𝐁𝐫𝐨..??🥲** ",
" **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐒𝐞𝐭 𝐇𝐚𝐢 𝐍𝐚🥺** ",
" **𝐁𝐡𝐚𝐢 𝐓𝐮𝐣𝐡𝐞 𝐘𝐚𝐚𝐝 𝐊𝐚𝐫 𝐑𝐡𝐚 𝐓𝐡𝐚 🤭** ",
" **𝐎𝐲𝐞 𝐊𝐚𝐢𝐬𝐞 𝐂𝐡𝐚𝐥 𝐑𝐚𝐡𝐚 𝐇𝐚𝐢 𝐒𝐚𝐛🤨** ",
" **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐰𝐚 𝐃𝐞𝐠𝐚 𝐊𝐲𝐚🙂** ",
" **𝐓𝐞𝐫𝐚 𝐍𝐚𝐦 𝐊𝐲𝐚 𝐡𝐚𝐢 𝐁𝐫𝐨..?🥲** ",
" **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐊𝐲𝐚 𝐁𝐡𝐚𝐢😋** ",
" **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐁𝐡𝐢 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐋𝐞 𝐋𝐨😍** ",
" **𝐓𝐞𝐫𝐚 𝐃𝐮𝐬𝐫𝐚 𝐀𝐜𝐜 𝐎𝐧𝐥𝐢𝐧𝐞 𝐇𝐚𝐢, 𝐃𝐞𝐤𝐡 𝐋𝐞😅** ",
" **𝐁𝐡𝐚𝐢 𝐃𝐨𝐬𝐭𝐢 𝐊𝐚𝐫𝐨𝐠𝐞 𝐊𝐲𝐚..??🤔** ",
" **𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
" **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐃𝐞𝐬𝐡𝐢 𝐖𝐚𝐥𝐚 𝐏𝐥𝐚𝐲 𝐊𝐫 𝐁𝐡𝐚𝐢😕** ",
" **𝐀𝐚𝐩 𝐊𝐡𝐚𝐧 𝐒𝐞 𝐇𝐨..??🙃** ",
" **𝐇𝐞𝐥𝐥𝐨 𝐁𝐡𝐚𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
" **𝐁𝐡𝐚𝐢 𝐊𝐤𝐫𝐡..?🤔** ",
" **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 [@mreccen_tric]?** ",
" **𝐂𝐡𝐚𝐥𝐨 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
" **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐢 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨😇** ",
" **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
" **𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐘𝐫🥺** ",
" **𝐎𝐲𝐞 𝐏𝐚𝐠𝐥𝐞 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
" **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚..?🤔** ",
" **𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 𝐁𝐫𝐨😜** ",
" **𝐁𝐡𝐚𝐢 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐓𝐡𝐚🙂** ",
" **𝐂𝐡𝐚𝐥 𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫😪** ",
" **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐘𝐚𝐫☺** ",
" **𝐇𝐞𝐥𝐥𝐨🙊** ",
" **𝐏𝐚𝐝𝐡𝐚𝐢 𝐊𝐡𝐚𝐭𝐦 𝐇𝐮𝐢..?😺** ",
" **𝐁𝐨𝐥 𝐍𝐚 𝐁𝐫𝐨🥲** ",
" **𝐘𝐞 𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢 𝐁𝐡𝐚𝐢😅** ",
" **𝐄𝐤 𝐏𝐢𝐜 𝐃𝐞𝐤𝐡𝐧𝐞 𝐊𝐨 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
" **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
" **𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
" **𝐁𝐫𝐨 𝐋𝐨𝐲𝐚𝐥 𝐇𝐮🙈** ",
" **𝐓𝐮 𝐁𝐨𝐥 𝐏𝐡𝐢𝐫 𝐃𝐞𝐤𝐡𝐭𝐞 𝐇𝐚𝐢𝐧👀** ",
" **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚 𝐉𝐚𝐦𝐚𝐧𝐚 𝐆𝐲𝐚 𝐁𝐡𝐚𝐢🙉** ",
" **𝐄𝐤 𝐆𝐚𝐧𝐚 𝐃𝐞 𝐃𝐨 𝐁𝐡𝐢 𝐁𝐚𝐝𝐞😹** ",
" **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐆𝐚𝐧𝐚 𝐏𝐥𝐚𝐲 𝐇𝐨 𝐑𝐚𝐡𝐚 𝐇𝐮😻** ",
" **𝐈𝐧𝐬𝐭𝐚 𝐒𝐜𝐫𝐨𝐥𝐥 𝐇𝐨 𝐑𝐚𝐡𝐞 𝐇𝐨..?🙃** ",
" **𝐍𝐮𝐦𝐛𝐞𝐫 𝐍𝐚 𝐃𝐞 𝐁𝐫𝐨😕** ",
" **𝐂𝐨𝐧𝐬𝐞 𝐒𝐨𝐧𝐠 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
" **𝐊𝐚𝐦 𝐒𝐚𝐫𝐚 𝐊𝐡𝐚𝐭𝐦 𝐇𝐮𝐚..?🙃** ",
" **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐁𝐫𝐨😊** ",
" **𝐇𝐞𝐲 [@eccentricexplorer]🧐** ",
" **𝐄𝐤 𝐂𝐡𝐨𝐭𝐚 𝐊𝐚𝐚𝐦 𝐇𝐚𝐢 𝐁𝐡𝐚𝐢..** ",
" **𝐀𝐛 𝐁𝐡𝐚𝐮 𝐍𝐚𝐡𝐢 𝐂𝐡𝐚𝐢𝐲𝐞, 𝐀𝐥𝐚𝐠 𝐇𝐨 𝐉𝐚😠** ",
" **𝐌𝐨𝐦-𝐃𝐚𝐝 𝐓𝐡𝐢𝐤 𝐇𝐚𝐢𝐧..?❤** ",
" **𝐊𝐲𝐚 𝐇𝐨𝐚 𝐁𝐫𝐨..?👱** ",
" **𝐁𝐡𝐚𝐢 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐚 𝐇𝐮 🤧❣️** ",
" **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚😏😏** ",
" **𝐒𝐚𝐜𝐡 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
" **𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐞 𝐘𝐚𝐫, 𝐍𝐚𝐫𝐚𝐳 𝐌𝐚𝐭 𝐇𝐨😒** ",
" **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** ",
" **𝐇𝐢𝐢👀** ",
" **𝐁𝐫𝐨 𝐉𝐞𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐓𝐨 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚🙈** ",
" **𝐀𝐚𝐣 𝐌𝐨𝐨𝐝 𝐎𝐟𝐟 𝐇𝐚𝐢 ☹️** ",
" **𝐁𝐫𝐨 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐞 𝐍𝐚 🥺🥺** ",
" **𝐊𝐲𝐚 𝐂𝐡𝐚𝐥 𝐑𝐚𝐡𝐚 𝐇𝐚𝐢👀** ",
" **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
" **𝐊𝐡𝐚𝐧 𝐒𝐞 𝐇𝐨 𝐁𝐫𝐨..?🤔** ",
" **𝐂𝐡𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐁𝐡𝐚𝐢🥺** ",
" **𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐘𝐫, 𝐏𝐚𝐤𝐤𝐚🥺🥺** ",
" **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐊𝐫𝐭𝐞 𝐁𝐫𝐨😕** ",
" **𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐁𝐡𝐨𝐭 𝐘𝐚𝐫😼** ",
" **𝐆𝐚𝐧𝐚 𝐆𝐚 𝐋𝐨 𝐙𝐫𝐚😸** ",
" **𝐂𝐡𝐚𝐥𝐨 𝐆𝐡𝐮𝐦 𝐊𝐞 𝐀𝐚𝐭𝐞 𝐇𝐚𝐢🙈** ",
" **𝐇𝐚𝐦𝐞𝐬𝐡𝐚 𝐇𝐚𝐬𝐭𝐞 𝐑𝐚𝐡𝐨 ✌️🤞** ",
" **𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐉𝐚𝐲𝐞𝐢𝐧𝐠𝐞 𝐊𝐲𝐚...?🥰** ",
" **𝐁𝐨𝐥 𝐍𝐚 𝐁𝐡𝐚𝐢, 𝐂𝐡𝐮𝐩 𝐊𝐲𝐮 𝐇𝐨🥺🥺** ",
" **𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐫 𝐃𝐨 🥲** ",
" **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
" **𝐂𝐡𝐚𝐥 𝐏𝐚𝐫𝐭𝐲 𝐊𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
" **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
" **𝐁𝐡𝐮𝐥 𝐍𝐚 𝐉𝐚 𝐁𝐡𝐚𝐢🥺** ",
" **𝐘𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:-[@filmdom_updates]🤭🤭** ",
" **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐞..? 😊** ",
" **𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐀𝐚𝐣🥺🥺** ",
" **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨🤗** ",
" **𝐃𝐢𝐥 𝐇𝐞 𝐄𝐤, 𝐓𝐨𝐝𝐧𝐚 𝐍𝐚𝐡𝐢 𝐇𝐨𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞😗😗** ",
" **𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
" **𝐌𝐲 𝐁𝐫𝐨 𝐎𝐰𝐧𝐞𝐫 { @mreccen_tric}🥰** ",
" **𝐊𝐚𝐡𝐚 𝐆𝐡𝐮𝐦 𝐆𝐲𝐞 𝐁𝐫𝐨😜** ",
" **𝐆𝐨𝐨𝐝 𝐍8 𝐁𝐡𝐚𝐢, 𝐑𝐚𝐚𝐭 𝐇𝐨 𝐆𝐲𝐢🥰** ",
]

VC_TAG = [
    "**𝐎𝚈𝙴 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰 𝐏𝙻𝚂🥲**",  # Neutral, already fine
    "**𝐉𝙾𝙸𝙽 𝐕𝙲 𝐅𝙰𝚂𝚃 𝐈𝚃𝚂 𝐈𝙼𝙿𝙾𝚁𝚃𝙰𝙽𝚃😬**",  # Masculine urgency
    "**𝐁𝚁𝙾 𝐕𝙲 𝐀𝙰 𝐉𝙰 𝐌𝘼𝙃𝙊𝙻 𝐁𝙽𝚁𝙰 𝐇⚡**",  # Changed "BABY" to bro vibe
    "**𝐁𝚁𝙾 𝐓𝚄𝙼 𝐁𝙷𝙸 𝐓𝙷𝙾𝚁𝙰 𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰😎**",  # Replaced flirty tone
    "**𝐎𝚈𝙴 𝐁𝚁𝙾 𝐕𝙲 𝐀𝙰 𝐄𝙺 𝐄𝙼 𝐇𝙰𝙸🤨**",  # Chamtu → Bro, to sound less childish
    "**𝐒𝚄𝙽𝙾 𝐕𝙲 𝐉𝙾𝙸𝙽 𝐊𝚁 𝐋𝙾🤣**",  # Light banter
    "**𝐕𝙲 𝐀𝙰 𝐉𝙰𝙾 𝐁𝚁𝙾 𝐄𝙺 𝐁𝙰𝚁😁**",  # More neutral
    "**𝐕𝙲 𝐂𝙷𝙰𝙻𝚄 𝐇𝙰𝙸, 𝐆𝙰𝙼𝙴 𝐓𝙰𝙿𝙆𝙾⚽**",  # Rephrased, same tone
    "**𝐕𝙲 𝐀𝙰𝙾 𝐍𝙰𝙷𝙸 𝐓𝙾 𝐁𝙰𝙽 𝐃𝙴𝚁𝚄𝙽𝙶𝙰🥺**",  # Fun threat
    "**𝐎𝙿 𝐁𝙍𝙾, 𝐕𝙲 𝐀𝙰 𝐉𝙰 𝐍𝙰, 𝐁𝙰𝙆𝗂 𝐁𝙰𝙳 𝐌𝙴 𝐃𝙴𝙺H𝙴𝗡𝗚𝗘😥**",  # Rewritten from flirty apology
    "**𝐕𝙲 𝐀𝙰 𝐍𝙰, 𝐄𝙺 𝐒𝙲𝙴𝙽𝙴 𝐃𝙸𝙺𝙷𝙰𝚃𝙰 𝐇𝚄🙄**",  # Same vibe, less flirty
    "**𝐕𝙲 𝐂𝙷𝙴𝙲𝙺 𝐊𝚁 𝐁𝚁𝙾, 𝐒𝙾𝙽𝙶 𝐏𝙻𝙰𝚈 𝐇𝙾 𝐑𝙷𝙰 𝐇?🤔**",  # Casual, neutral
    "**𝐕𝙲 𝐅𝚃. 𝐊𝚁 𝐋𝙴 𝐁𝚁𝙾, 𝐓𝙷𝙾𝚁𝙰 𝐃𝙴𝙻𝙰𝚈 𝐂𝙷𝙰𝙻 𝐅𝙸𝚃 𝐇🙂**"  # Casual masculine pitch
]



@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐢𝐬 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 ����, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧... ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/tagall  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
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

@app.on_message(filters.command(["tagoff", "tagstop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
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
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐧 𝐀𝐝𝐦𝐢𝐧 ����, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("🌷𝐓𝐀𝐆 𝐀𝐋𝐋 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 🎉")
