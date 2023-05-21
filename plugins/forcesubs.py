import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import config
from tools.database import db
LOGS = logging.getLogger(__name__)

MUST_JOIN = config.MUST_JOIN
force_subs = config.FORCE_SUBS

# MUST_JOIN = set_channel()
# force_subs = set_fsub()

async def set_global_channel():
    global MUST_JOIN
    MUST_JOIN = await db.get_fsub_channel()
    
async def set_global_fsub():
    global force_subs
    force_subs = await db.get_fsub()

async def must_join_channel(bot: Client, msg: Message):
    await set_global_channel()
    await set_global_fsub()
    if not force_subs: 
        return
    try:
       
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            
            try:
                
                if type(MUST_JOIN) == str:
                    link = "https://t.me/" + MUST_JOIN
                    chat_info = await bot.get_chat(MUST_JOIN)
                    name = chat_info.title
                    await msg.reply(
                        f"Please join [{name}]({link}) to use me.\nAfter joining start bot again !",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(f"🥀 Join {name} 🥀", url=link)]
                        ])
                    )
                    await msg.stop_propagation()

                elif type(MUST_JOIN) == int:
                    chat_info = await bot.get_chat(MUST_JOIN)
                    name = chat_info.title
                    link = chat_info.invite_link
                    await msg.reply(
                        f"🥀 Please join [{name}]({link}) to use me.\nAfter joining start bot again 🥀\n🌿 If You Don't Join Our Channel Then Leave The Bot 🥀",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton(f"🥀 Join {name} 🥀", url=link)]
                        ])
                    )
                    await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        await bot.send_message(config.LOG_CHANNEL,f"🥀 I'm not admin in the {MUST_JOIN} chat please make me admin to use force subscribe feature in your bot 😁")
        LOGS.info(f"I'm not admin in the {MUST_JOIN} chat please make me admin to use force subscribe feature in your bot!")