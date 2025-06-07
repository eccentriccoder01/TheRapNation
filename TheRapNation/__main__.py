import asyncio
import importlib
import os
from flask import Flask, request
from pyrogram import Client
from pytgcalls.exceptions import NoActiveGroupCall

import config
from TheRapNation import LOGGER, app as pyro_app, userbot
from TheRapNation.core.call import Hotty
from TheRapNation.misc import sudo
from TheRapNation.plugins import ALL_MODULES
from TheRapNation.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# Flask App for Webhooks
flask_app = Flask(__name__)
loop = asyncio.get_event_loop()

# Import all plugin modules
for all_module in ALL_MODULES:
    importlib.import_module("TheRapNation.plugins" + all_module)

@flask_app.route("/", methods=["GET"])
def home():
    return "TheRapNation Bot is running!"

@flask_app.route(f"/{config.BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    loop.create_task(pyro_app.process_update(update))
    return "Webhook received!"

async def init():
    if (
        not config.STRING1 and not config.STRING2 and not config.STRING3 and
        not config.STRING4 and not config.STRING5
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
    except Exception as e:
        LOGGER("TheRapNation").warning(f"Error fetching banned users: {e}")

    await pyro_app.start()
    await userbot.start()
    await Hotty.start()

    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("TheRapNation").error(
            "Please turn on the videochat of your log group/channel.\nStopping Bot..."
        )
        exit()
    except Exception as e:
        LOGGER("TheRapNation").warning(f"Stream call error: {e}")

    await Hotty.decorators()

    webhook_url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{config.BOT_TOKEN}"
    await pyro_app.set_webhook(webhook_url)

    LOGGER("TheRapNation").info("Bot started via webhook successfully!")

def run():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    loop.run_until_complete(init())
    run()
