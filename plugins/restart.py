import logging
import os
from tools.database import db
from pyrogram import Client, filters
import config
LOGS = logging.getLogger(__name__)

@Client.on_message(filters.command("restart"))
async def restart_bot(_, message):
    if message.from_user.id not in config.AUTH_USERS:
        # await m.delete()
        return
    try:
        msg = await message.reply_text("🔁 Restarting bot...")
        LOGS.info("BOT RESTARTED !!")
    except BaseException as err:
        LOGS.error(f"{err}")
        return
    await msg.edit_text("✅ The robot has restarted ! \n\n Active again within 5-10 seconds.")
    os.system(f"kill -9 {os.getpid()} && python3 startup.py")
    


@Client.on_message(filters.command("quit"))
async def restart_bot(_, message):
    if message.from_user.id not in config.AUTH_USERS:
        
        return
    try:
        msg = await message.reply_text("❌ Stopping bot...❌")
        LOGS.info("Bot stopped !!")
    except BaseException as err:
        LOGS.error(f"{err}")
        return
    await msg.edit_text("✅ The bot has been suspended !")
    os.system(f"kill -9 {os.getpid()}")