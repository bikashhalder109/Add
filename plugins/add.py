import asyncio
import logging
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait as FloodWait1
from pyrogram import Client as Client1, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import time
import datetime
import config
from plugins.eval import remove_if_exists
from tools.database import Database
from pyromod.helpers import ikb
from tools.main import bot
LOGS = logging.getLogger(__name__)
db = Database(config.DB_URL, config.DB_NAME)


# api = ""
# hash = ""

import re
def if_url(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            #r'^t.me|'
            r't.me|'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    
    string = url
    x = re.match(regex, string) is not None 
    if x:
        if "t.me" in string:
            xu = string.split("t.me/")[1]
            return f"@{xu}"
    elif "@" in string:
        xu = string
        return xu


@Client.on_message(filters.private & filters.command("invite"))
async def NewChat(client, msg):
    try:
        chat = msg.chat
        bgt = await msg.reply_text(".... BIKASH GADGETS TECH ....")
        await edit_bgtbots(bgt)
        userr = msg.from_user.id
        if not await db.get_session(userr):
            return await bgt.edit_text("please /login to use this feature.")

        await bgt.delete()
        while True:
            src_raw = await bot.ask(chat.id, "Now send me a public group link from where you want to scrape and transfer members from...")
            if not src_raw.text:
                continue
            if await is_cancel(msg, src_raw.text):
                return
            src = if_url(src_raw.text)
            
            dest_raw = await bot.ask(chat.id, "Now send me a link to a public group where you want to add members..")
            if await is_cancel(msg, dest_raw.text):
                return
            dest = if_url(dest_raw.text)
            quant_raw = await bot.ask(chat.id, "Send me the quantity now. How many members do you want to add to your group?\n\n For example send : 5\n\n For the security of your accounts against extension ban, please provide us with a number less than 20 digits ")
            if await is_cancel(msg, quant_raw.text):
                return
            quant = int(quant_raw.text)
            type_raw = await bot.ask(chat.id, f'Now choose which type of member you want to scrape from a group `{src}`\n\n To transfer active 👤 members 👤 send  `a`\n\n To transfer members 👥 mixed 👥 send `m`. \n\n Send : `a` (If you want active members)\n Send : `m` (If you want Mixed members)')
            if await is_cancel(msg, type_raw.text):
                return
            type = type_raw.text.lower()

            confirm = await bot.ask(chat.id, f'You want to add `{quant}` {"`👤 Active members 👤`" if type == "a" else "`👥 Mixed members 👥`"} I set `{src}` to your group `{dest}`\n\n`Is this sure to add? (y / n):` \n\n Send : `y` (If the answer is yes)\n Send : `n` (If the answer is no)')
            if await is_cancel(msg, confirm.text):
                return
            confirm = confirm.text.lower()
            if confirm == "y":
                break
        try:

            await add(msg, src=src, dest=dest, count=quant, type=type)
        except Exception as e:
            return await msg.reply_text(f"**ERROR:** `{str(e)}`",reply_markup=keyboard)
    except Exception as e:
        return await msg.reply_text(f"**ERROR:** `{str(e)}`",reply_markup=keyboard)


async def is_cancel(msg: Message, text: str):
    if text.startswith("/cancel"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/login"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/start"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/restart"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/help"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/invite"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/status"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/"):
        await msg.reply("Login Cancelled.")
        return True
    return False


async def type_(text: str):
    text = text.lower()
    if text == "y":
        return True
    elif text == "n":
        return False
    else:
        return False


async def edit_bgtbots(bgt):
    await bgt.edit_text("**🇮🇳️.... Bgt .... 🇮🇳️**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**.🥀️... BGt ...🥀️.**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**..🌷️.. BGT ..🌷️..**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**...🌹️. bgt .🌹️...**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**....🌺️ BGT 🌺️....**")
    await asyncio.sleep(0.5)


async def edit_starting(bgt):
    await bgt.edit_text("**🇮🇳️.... STARTING CLIENT ....🇮🇳️**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**.🥀... STARTING CLIENT ...🥀️.**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**..🌷.. STARTING CLIENT ..🌷️..**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**...🌹. STARTING CLIENT .🌹️...**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**....🌺️ STARTING CLIENT 🌺️....**")
    await asyncio.sleep(0.5)


async def edit_ini(bgt):
    await bgt.edit_text("**🇮🇳️........🇮🇳️**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**.🌹......🌹️.**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**..🌷....🌷️..**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**...🌺️..🌺️...**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**....🥀️🥀️....**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("🇮🇳")
    await asyncio.sleep(0.4)

async def edit_active(bgt):
    await bgt.edit_text("**🌷.... STARTING ACTIVE MEMBER ADDING ....🌷️**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**.🌹... STARTING ACTIVE MEMBER ADDING ...🌹️.**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**..🌺️.. STARTING ACTIVE MEMBER ADDING ..🌺️..**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**...🥀. STARTING ACTIVE MEMBER ADDING .🥀️...**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**....🇮🇳️ STARTING ACTIVE MEMBER ADDING 🇮🇳️....**")
    await asyncio.sleep(0.5)

async def edit_mixed(bgt):
    await bgt.edit_text("**💕️.... STARTING MIXED MEMBER ADDING ....💕️**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**.🌹️... STARTING MIXED MEMBER ADDING ...🌹️.**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**..🌺️.. STARTING MIXED MEMBER ADDING ..🌺️..**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**...🥀️. STARTING MIXED MEMBER ADDING .🥀️...**")
    await asyncio.sleep(0.3)
    await bgt.edit_text("**....🇮🇳️ STARTING MIXED MEMBER ADDING 🇮🇳️....**")
    await asyncio.sleep(0.5)

keyboard = ikb([
        [('🥀 Updates 🥀', 'https://t.me/BikashGadgetsTech',"url")], 

        [('🥀 Support 🥀','https://t.me/Bgt_Chat',"url")]
                ])

async def add(msg, src, dest, count: int, type):
    userid = msg.from_user.id
    bgt = await msg.reply_text("**........**")
    await edit_ini(bgt)

    try:

        cc = 0

        session = await db.get_session(userid)
        api = await db.get_api(userid) 
        hash = await db.get_hash(userid) 
        # print(session)
        # session = str(session)

        app = Client(name= userid,session_string=session, api_id=api, api_hash=hash)
        await bgt.edit_text("**.... STARTING CLIENT ....**")
        
        await app.start()
        await edit_starting(bgt)
        # print('\n\napp started...')
        # await asyncio.sleep(0.5)

        # source chat

        chat = await app.get_chat(src)
        schat_id = chat.id
        await app.join_chat(schat_id)
        # dest chat
        xx = await app.get_chat(dest)
        tt = xx.members_count
        dchat_id = xx.id
        await app.join_chat(dchat_id)
        start_time = time.time()
        await asyncio.sleep(3)
    except Exception as e:
                        e = str(e)
                               # await err(e=e,app=app,bgt=bgt)
                        if "Client has not been started yet" in e:
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Client has not been started yet",reply_markup=keyboard)
                        elif "403 USER_PRIVACY_RESTRICTED" in e:
                            await bgt.edit_text("failed to add because of The user's privacy settings",reply_markup=keyboard)
                            await asyncio.sleep(1)
                        elif "400 CHAT_ADMIN_REQUIRED" in e:
                            await bgt.edit_text("failed to add because of This method requires chat admin privileges.\n\nplease make your account admin on the group and try again",reply_markup=keyboard)
                        elif "400 INVITE_REQUEST_SENT" in e:
                            
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("hey i cant scrape/add members from a group where i need admin approval to join chat.",reply_markup=keyboard)
                        elif "400 PEER_FLOOD" in e:
                            # 
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Adding stopped due to 400 PEER_FLOOD\n\nyour account is limited please wait sometimes then try again.",reply_markup=keyboard)
                        elif "401 AUTH_KEY_UNREGISTERED" in e:
                            
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("please login again to use this feature",reply_markup=keyboard)
                        elif "403 CHAT_WRITE_FORBIDDEN" in e:
                            
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("You don't have rights to send messages in this chat\nPlease make user account admin and try again",reply_markup=keyboard)
                        elif "400 CHANNEL_INVALID" in e:
                            
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The source or destination username is invalid",reply_markup=keyboard)
                        elif "400 USERNAME_NOT_OCCUPIED" in e:
                            
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The username is not occupied by anyone please check the username or userid that you have provided",reply_markup=keyboard)
                        elif "401 SESSION_REVOKED" in e:
                            
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("you have terminated the login session from the user account \n\nplease login again",reply_markup=keyboard)
        
                        return await bgt.edit_text(f"**ERROR:** `{str(e)}`",reply_markup=keyboard)

    if type == "a":
        try:
            await bgt.edit_text("**.... STARTING ACTIVE MEMBER ADDING ....**")
            await edit_active(bgt)
            await asyncio.sleep(0.5)
            # async for member in app.iter_chat_members(schat_id):
            async for member in app.get_chat_members(schat_id):
                user = member.user

                s = ["RECENTLY","ONLINE"]
                if user.is_bot:
                    pass
                else:
                    b = (str(user.status)).split('.')[1]
                    if b in s:
      
                # s = ["online", "recently"]
                
                # if user.status in s:
                        try:

                            user_id = user.id

                            await bgt.edit_text(f'TRYING TO ADD: `{user_id}`')

                            if await app.add_chat_members(dchat_id, user_id):
                                cc = cc+1
                                await bgt.edit_text(f'ADDED: `{user_id}`')

                                await asyncio.sleep(5)
                        except FloodWait1 as fl:
                            t = "FLOODWAIT DETECTED IN USER ACCOUNT\n\nSTOPPED ADDING PROCESS"

                            await bgt.edit_text(t)
                            x2 = await app.get_chat(dchat_id)
                            t2 = x2.members_count
                            completed_in = datetime.timedelta(
                            seconds=int(time.time() - start_time))
                            ttext = f"""
<u>**✨ Stopped adding process due to Floodwait of {fl.value}s ✨**</u>

    ┏━━━━━━━━━━━━━━━━━┓
    ┣✨ Added to chat Id: `{dchat_id}`
    ┣✨ Previous chat member count : **{tt}**
    ┣✨ Current chat member count : **{t2}**
    ┣✨ Total users added : **{cc}**
    ┣✨ Total time taken : **{completed_in}**s
    ┗━━━━━━━━━━━━━━━━━┛
                                """

                            await app.leave_chat(src)
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text(ttext,reply_markup=keyboard)
                        except Exception as e:
                            e = str(e)
                                # await err(e=e,app=app,bgt=bgt)
                            if "Client has not been started yet" in e:
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("Client has not been started yet",reply_markup=keyboard)
                            elif "403 USER_PRIVACY_RESTRICTED" in e:
                                await bgt.edit_text("failed to add because of The user's privacy settings")
                                await asyncio.sleep(1)
                            elif "400 CHAT_ADMIN_REQUIRED" in e:
                                await bgt.edit_text("failed to add because of This method requires chat admin privileges.\n\nplease make your account admin on the group and try again",reply_markup=keyboard)
                            elif "400 INVITE_REQUEST_SENT" in e:
                                await app.stop()
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("hey i cant scrape/add members from a group where i need admin approval to join chat.",reply_markup=keyboard)
                            elif "400 PEER_FLOOD" in e:
                                await app.stop()
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("Adding stopped due to 400 PEER_FLOOD\n\nyour account is limited please wait sometimes then try again.",reply_markup=keyboard)
                            elif "401 AUTH_KEY_UNREGISTERED" in e:
                                await app.stop()
                                await db.set_session(msg.from_user.id, "")
                                await db.set_login(msg.from_user.id,False)
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("please login again to use this feature",reply_markup=keyboard)
                            elif "403 CHAT_WRITE_FORBIDDEN" in e:
                                await app.stop()
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("You don't have rights to send messages in this chat\nPlease make user account admin and try again",reply_markup=keyboard)
                            elif "400 CHANNEL_INVALID" in e:
                                await app.stop()
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("The source or destination username is invalid",reply_markup=keyboard)
                            elif "400 USERNAME_NOT_OCCUPIED" in e:
                                await app.stop()
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("The username is not occupied by anyone please check the username or userid that you have provided",reply_markup=keyboard)
                            elif "401 SESSION_REVOKED" in e:
                                await app.stop()
                                await db.set_session(msg.from_user.id, "")
                                await db.set_login(msg.from_user.id,False)
                                remove_if_exists(f"{msg.from_user.id}_account.session")
                                return await bgt.edit_text("you have terminated the login session from the user account \n\nplease login again",reply_markup=keyboard)
          
                            else:
                                await bgt.edit_text(f'FAILED TO ADD \n\n**ERROR:** `{str(e)}`')
                                await asyncio.sleep(5)

                        if cc == count:
                            x2 = await app.get_chat(dchat_id)
                            t2 = x2.members_count
                            completed_in = datetime.timedelta(
                            seconds=int(time.time() - start_time))
                            ttext = f"""
<u>**✨ Successfully completed adding process ✨**</u>

    ┏━━━━━━━━━━━━━━━━━┓
    ┣✨ Added to chat Id: `{dchat_id}`
    ┣✨ Previous chat member count : **{tt}**
    ┣✨ Current chat member count : **{t2}**
    ┣✨ Total users added : **{cc}**
    ┣✨ Total time taken : **{completed_in}**s
    ┗━━━━━━━━━━━━━━━━━┛
                                """

                            await app.leave_chat(src)
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text(ttext,reply_markup=keyboard)

        except Exception as e:
                        e = str(e)
                               # await err(e=e,app=app,bgt=bgt)
                        if "Client has not been started yet" in e:
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Client has not been started yet",reply_markup=keyboard)
                        elif "403 USER_PRIVACY_RESTRICTED" in e:
                            await bgt.edit_text("failed to add because of The user's privacy settings",reply_markup=keyboard)
                            await asyncio.sleep(1)
                        elif "400 CHAT_ADMIN_REQUIRED" in e:
                            await bgt.edit_text("failed to add because of This method requires chat admin privileges.\n\nplease make your account admin on the group and try again",reply_markup=keyboard)
                        elif "400 INVITE_REQUEST_SENT" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("hey i cant scrape/add members from a group where i need admin approval to join chat.",reply_markup=keyboard)
                        elif "400 PEER_FLOOD" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Adding stopped due to 400 PEER_FLOOD\n\nyour account is limited please wait sometimes then try again.",reply_markup=keyboard)
                        elif "401 AUTH_KEY_UNREGISTERED" in e:
                            await app.stop()
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("please login again to use this feature",reply_markup=keyboard)
                        elif "403 CHAT_WRITE_FORBIDDEN" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("You don't have rights to send messages in this chat\nPlease make user account admin and try again",reply_markup=keyboard)
                        elif "400 CHANNEL_INVALID" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The source or destination username is invalid",reply_markup=keyboard)
                        elif "400 USERNAME_NOT_OCCUPIED" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The username is not occupied by anyone please check the username or userid that you have provided",reply_markup=keyboard)
                        elif "401 SESSION_REVOKED" in e:
                            await app.stop()
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("you have terminated the login session from the user account \n\nplease login again",reply_markup=keyboard)
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text(f"**ERROR:** `{str(e)}`",reply_markup=keyboard)


    if type != "a":
        try:
            await bgt.edit_text("**.... STARTING MIXED MEMBER ADDING ....**")
            await edit_mixed(bgt)
            async for member in app.get_chat_members(schat_id):
                user = member.user
                  # s = ["online" , "recently"]
                  # if user.status in s:
                try:

                    user_id = user.id

                    await bgt.edit_text(f'TRYING TO ADD: `{user_id}`')

                    if await app.add_chat_members(dchat_id, user_id):
                        cc = cc+1
                        await bgt.edit_text(f'ADDED: `{user_id}`')

                        await asyncio.sleep(5)
                except FloodWait1 as fl:
                    t = "FLOODWAIT DETECTED IN USER ACCOUNT\n\nSTOPPED ADDING PROCESS"

                    await bgt.edit_text(t)
                    x2 = await app.get_chat(dchat_id)
                    t2 = x2.members_count
                    completed_in = datetime.timedelta(
                    seconds=int(time.time() - start_time))
                    ttext = f"""
<u>**✨ Stopped adding process due to Floodwait of {fl.value}s ✨**</u>

    ┏━━━━━━━━━━━━━━━━━┓
    ┣✨ Added to chat Id: `{dchat_id}`
    ┣✨ Previous chat member count : **{tt}**
    ┣✨ Current chat member count : **{t2}**
    ┣✨ Total users added : **{cc}**
    ┣✨ Total time taken : **{completed_in}**s
    ┗━━━━━━━━━━━━━━━━━┛
    
                        """

                    await app.leave_chat(src)
                    await app.stop()
                    remove_if_exists(f"{msg.from_user.id}_account.session")
                    return await bgt.edit_text(ttext,reply_markup=keyboard)
                except Exception as e:
                    e = str(e)
                    # await err(e=e,app=app,bgt=bgt)

                    if "Client has not been started yet" in e:
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("Client has not been started yet\n\nplease start the adding process again.",reply_markup=keyboard)
                    elif "403 USER_PRIVACY_RESTRICTED" in e:
                        await bgt.edit_text("failed to add because of The user's privacy settings",reply_markup=keyboard)
                        await asyncio.sleep(1)
                    elif "400 CHAT_ADMIN_REQUIRED" in e:
                        await bgt.edit_text("failed to add because of This method requires chat admin privileges.\n\nplease make your account admin on the group and try again",reply_markup=keyboard)
                    elif "400 INVITE_REQUEST_SENT" in e:
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("hey i cant scrape/add members from a group where i need admin approval to join chat.",reply_markup=keyboard)
                    elif "400 PEER_FLOOD" in e:
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("Adding stopped due to 400 PEER_FLOOD\n\nyour account is limited please wait sometimes then try again.",reply_markup=keyboard)
                    elif "401 AUTH_KEY_UNREGISTERED" in e:
                        await app.stop()
                        await db.set_session(msg.from_user.id, "")
                        await db.set_login(msg.from_user.id,False)
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("please login again to use this feature",reply_markup=keyboard)
                    elif "403 CHAT_WRITE_FORBIDDEN" in e:
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("You don't have rights to add members in this chat\nPlease make user your account admin and try again",reply_markup=keyboard)
                    elif "400 CHANNEL_INVALID" in e:
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("The source or destination username is invalid",reply_markup=keyboard)
                    elif "400 USERNAME_NOT_OCCUPIED" in e:
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("The username is not occupied by anyone please check the username or userid that you have provided",reply_markup=keyboard)
                    elif "401 SESSION_REVOKED" in e:
                        await app.stop()
                        await db.set_session(msg.from_user.id, "")
                        await db.set_login(msg.from_user.id,False)
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text("you have terminated the login session from the user account \n\nplease login again",reply_markup=keyboard)
                    else:
                        await bgt.edit_text(f'FAILED TO ADD \n\n**ERROR:** `{str(e)}`')
                        await asyncio.sleep(5)

                if cc == count:
                    x2 = await app.get_chat(dchat_id)
                    t2 = x2.members_count
                    completed_in = datetime.timedelta(
                    seconds=int(time.time() - start_time))
                    ttext = f"""
<u>**✨ Successfully completed adding process ✨**</u>

    ┏━━━━━━━━━━━━━━━━━┓
    ┣✨ Added to chat Id: `{dchat_id}`
    ┣✨ Previous chat member count : **{tt}**
    ┣✨ Current chat member count : **{t2}**
    ┣✨ Total users added : **{cc}**
    ┣✨ Total time taken : **{completed_in}**s
    ┗━━━━━━━━━━━━━━━━━┛
                        """

                    await app.leave_chat(src)
                    await app.stop()
                    remove_if_exists(f"{msg.from_user.id}_account.session")
                    return await bgt.edit_text(ttext,reply_markup=keyboard)

        except Exception as e:
                        e = str(e)
                               # await err(e=e,app=app,bgt=bgt)
                        if "Client has not been started yet" in e:
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Client has not been started yet",reply_markup=keyboard)
                        elif "403 USER_PRIVACY_RESTRICTED" in e:
                            await bgt.edit_text("failed to add because of The user's privacy settings",reply_markup=keyboard)
                            await asyncio.sleep(1)
                        elif "400 CHAT_ADMIN_REQUIRED" in e:
                            await bgt.edit_text("failed to add because of This method requires chat admin privileges.\n\nplease make your account admin on the group and try again",reply_markup=keyboard)
                        elif "400 INVITE_REQUEST_SENT" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("hey i cant scrape/add members from a group where i need admin approval to join chat.",reply_markup=keyboard)
                        elif "400 PEER_FLOOD" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("Adding stopped due to 400 PEER_FLOOD\n\nyour account is limited please wait sometimes then try again.",reply_markup=keyboard)
                        elif "401 AUTH_KEY_UbgtEGISTERED" in e:
                            await app.stop()
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("please login again to use this feature",reply_markup=keyboard)
                        elif "403 CHAT_WRITE_FORBIDDEN" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("You don't have rights to send messages in this chat\nPlease make user account admin and try again",reply_markup=keyboard)
                        elif "400 CHANNEL_INVALID" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The source or destination username is invalid",reply_markup=keyboard)
                        elif "400 USERNAME_NOT_OCCUPIED" in e:
                            await app.stop()
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("The username is not occupied by anyone please check the username or userid that you have provided",reply_markup=keyboard)
                        elif "401 SESSION_REVOKED" in e:
                            await app.stop()
                            await db.set_session(msg.from_user.id, "")
                            await db.set_login(msg.from_user.id,False)
                            remove_if_exists(f"{msg.from_user.id}_account.session")
                            return await bgt.edit_text("you have terminated the login session from the user account \n\nplease login again",reply_markup=keyboard)
                        await app.stop()
                        remove_if_exists(f"{msg.from_user.id}_account.session")
                        return await bgt.edit_text(f"**ERROR:** `{str(e)}`",reply_markup=keyboard)