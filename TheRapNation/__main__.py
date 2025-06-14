import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TheRapNation import LOGGER, app, userbot
from TheRapNation.core.call import Hotty
from TheRapNation.misc import sudo
from TheRapNation.plugins import ALL_MODULES
from TheRapNation.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from TheRapNation.plugins.tools.clone import restart_bots




async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("TheRapNation.plugins" + all_module)
    LOGGER("TheRapNation.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://tinyurl.com/26c6xlo3")
    except NoActiveGroupCall:
        LOGGER("TheRapNation").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("TheRapNation").info(
        "ᴊᴏɪɴ @The_Rap_Nation , @eccentricexplorer ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TheRapNation").info("Stopping The Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
