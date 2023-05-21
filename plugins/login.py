import asyncio
import os
import time
from plugins.adder2 import edit_bgtbots
from tools.main import bot
from pyromod import listen
from asyncio.exceptions import TimeoutError
from pyromod.helpers import ikb
from pyrogram import Client, filters
from pyrogram import Client as Client1
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from pyrogram.errors import (
    SessionPasswordNeeded as SessionPasswordNeeded1, FloodWait as FloodWait1,
    PhoneNumberInvalid as PhoneNumberInvalid1 , ApiIdInvalid as ApiIdInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1, PhoneCodeExpired as PhoneCodeExpired1
)
from tools.database import Database
import config
db = Database(config.DB_URL, config.DB_NAME)

PHONE_NUMBER_TEXT = (
    "🥀 Now send an Telegram account phone number 🌿 your international format. 🥀 \n"
     "🥀 Include the country code. Example : ** +9186053912xx ** 🥀\n\n"
     "📍 Click : /cancel  to cancel ❌."
)

API_TEXT = (
    "🥀 Send your API ...\n\n🥀 If you do not know where to get API 🌿\n🥀 1- Go to this Telegram site 👇\n http://my.telegram.org \n🥀 2- Copy the API and then send it here 🥀"
)

HASH_TEXT = (
    "🥀 Send  api Hash \n\n 🥀 If you don't know where to get it api Hash \n🥀 1- Go to this Telegram site👇\n🥀 http://my.telegram.org  \n🥀 2- Copy the api hash and then send it here 🥀"
)

@bot.on_message(filters.private & filters.command("login"))
async def genStr(_, msg: Message):
    bgt = await msg.reply_text("**.... Bikash Gadgets Tech ....**")
    await edit_bgtbots(bgt)
    await asyncio.sleep(0.4)
    await bgt.delete()
    await msg.reply("🥀 Hey Dear \n {}! For more security of your account, you must provide me with api_id and api_hash to log into your account 🥀\n\n⚠️ Please login to your Fake account, do not use your real account ⚠️\n\n📍 See how to get api id , api Hash \n\n ️https://youtu.be/cVHwiLwhoFk".format(msg.from_user.mention))
    await asyncio.sleep(2)
    chat = msg.chat
    api = await bot.ask(
        chat.id, API_TEXT)
    
    if await is_cancel(msg, api.text):
        return
    try:
        check_api = int(api.text)
    except Exception:
        await msg.reply("`APP_ID` invalid.\n Click on /login to restart again.")
        return
    api_id = api.text
    hash = await bot.ask(chat.id, HASH_TEXT)
    if await is_cancel(msg, hash.text):
        return
    if not len(hash.text) >= 30:
        await msg.reply("`api_Hash` invalid\n click on /login to restart again")
        return
    api_hash = hash.text
    while True:
        number = await bot.ask(chat.id, PHONE_NUMBER_TEXT)
        if not number.text:
            continue
        if await is_cancel(msg, number.text):
            return
        phone = number.text
        confirm = await bot.ask(chat.id, f'`this "{phone}" right? (y/n):` \n\nSend : `y` (If the number is correct, send it y )\nSend: `n` (If the number is wrong, send it n)')
        if await is_cancel(msg, confirm.text):
            return
        confirm = confirm.text.lower()
        if confirm == "y":
            break
    try:
        client = Client1(f"{chat.id}_account", api_id=api_id, api_hash=api_hash,in_memory=True)
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`\nPress /login to Start again.")
        return
    try:
        await client.connect()
    except ConnectionError:
        await client.disconnect()
        await client.connect()
    try:
        code = await client.send_code(phone)
        await asyncio.sleep(1)
    except FloodWait1 as e:
        await msg.reply(f"You account have Floodwait of {e.value} Seconds. Please try after {e.value} Seconds")
        return
    except ApiIdInvalid1:
        await msg.reply("APP ID and API Hash are Invalid.\n\nPress /login to Start again.")
        return
    except PhoneNumberInvalid1:
        await msg.reply("Your number is incorrect.\n\nSend /login to Start Again.")
        return
    try:
        a = """
A five-digit code is sent to your phone number.
Please send the code in the format this 1 2 3 4 5. (a space between each number!) \n
If the Bot does not send an OTP, try restarting and starting the task again with the /start command to the Bot.
Press /cancel to cancel.."""
        otp = await bot.ask(chat.id, a
                    , timeout=300
                    )

    except TimeoutError:
        await msg.reply("The time limit is 5 minutes.\nClick /login to start over")
        return
    if await is_cancel(msg, otp.text):
        return
    otp_code = otp.text
    try:
        await client.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except PhoneCodeInvalid1:
        await msg.reply("Invalid code. \n\nClick /login to start Again..")
        return
    except PhoneCodeExpired1:
        await msg.reply("Code is Expired.\n\nPress /login to Start again.")
        return
    except SessionPasswordNeeded1:
        try:
            two_step_code = await bot.ask(
                chat.id, 
                "Your account has two-step verification.\nSend a two-step verification code or.\n\nPress /cancel to cancel.",
                timeout=300
            )
        except TimeoutError:
            await msg.reply("`Time limit reached of 5 min.\n\nPress /login to Start again.`")
            return
        if await is_cancel(msg, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await client.check_password(new_code)
        except Exception as e:
            await msg.reply(f"**ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`")
        return
    try:
        session_string = await client.export_session_string()
        await bot.send_message(chat.id,"✅ Your account is successfully connected",)
        await db.set_session(chat.id, session_string)
        await db.set_api(chat.id,api_id)
        await db.set_hash(chat.id,api_hash)
        await db.set_login(chat.id,True)
        await client.disconnect()
    except Exception as e:
        await bot.send_message(chat.id ,f"**ERROR:** `{str(e)}`")
        return





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
    elif text.startswith("/memadd"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/status"):
        await msg.reply("Login Cancelled.")
        return True
    elif text.startswith("/"):
        await msg.reply("Login Cancelled.")
        return True




@Client.on_message(filters.private & filters.command("status"))
async def logoutt(client, message:Message):
    bgt = await message.reply_text("checking...")
    user_id = message.from_user.id
    if await db.get_session(user_id):

        try:    
            session = await db.get_session(user_id) 
            api_id = await db.get_api(user_id) 
            api_hash = await db.get_hash(user_id) 
            app = Client(name = user_id,session_string=f"{session}", api_id = api_id, api_hash = api_hash,in_memory=True) 
            await app.start()
            await app.get_me()
            xx = await app.get_me()
            op = xx.first_name
                # ox = xx.username
            id = xx.id
            await app.stop()

            await bgt.edit_text(f'USER DETAILS\n\nName: {op}\n\nUser Id: {id}',
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    f"login status {'✅'if ((await db.get_session(user_id)) ) else '❎' }",
                                    callback_data="xyz",
                                )
                            ],
                            [InlineKeyboardButton(
                                f"{'Logout'if ((await db.get_session(user_id)) ) else 'Please Login To Use Adding Feature.' }", callback_data= f"{'Logout'if ((await db.get_session(user_id)) ) else 'Login' }",
                                
                                )
                            ],
                            [InlineKeyboardButton("close", callback_data="close")],
                        ]
                    ),)
        except ApiIdInvalid1:
            try:
                session = await db.get_session(user_id) 
                app = Client(name = user_id,session_string=f"{session}", api_id = config.API_ID, api_hash = config.API_HASH)
                await app.start()
                await app.get_me()
                xx = await app.get_me()
                op = xx.first_name
                # ox = xx.username
                id = xx.id
                await app.stop()
                keyboard = ikb([
        [(f"login status {'✅'if ((await db.get_session(user_id)) ) else '❎' }", f'xyz')], 
        [(f"{'Logout'if ((await db.get_session(user_id)) ) else 'Please Login To Use Adding Feature.' }",f"{'Logout'if ((await db.get_session(user_id)) ) else 'Login' }")],
        [("close","close")]
                    ])
                await bgt.edit_text(f'USER DETAILS\n\nName: {op}\n\nUser Id: {id}',
                reply_markup=keyboard)
                    
            except Exception as e:
                return await bgt.edit_text(f'**Error** : {e}')
        except Exception as e:
            return await bgt.edit_text(f'**Error** : {e}')
        

    else:        
        keyboard = ikb([
        [(f"login status {'✅'if ((await db.get_session(user_id)) ) else '❎' }", f'xyz')], 
        [(f"{'Logout'if ((await db.get_session(user_id)) ) else 'Please Login To Use Adding Feature.' }",f"{'Logout'if ((await db.get_session(user_id)) ) else 'Login' }")],
        [("close","close")]
                    ])
        await bgt.edit_text( 'Please Login to use all the bot features.',
                reply_markup=keyboard)
                
@Client.on_callback_query(filters.regex("Logout"))
async def cb_data_logout(client, update):
    user_id = update.from_user.id
    
    await update.message.edit_text(
            text='Are you sure to sign out?',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        f"Yes",
                        callback_data="yes",
                    )
                ],
              
                [InlineKeyboardButton("close", callback_data="close")],
            ]
        ),)


@Client.on_callback_query(filters.regex("yes"))
async def cb_data_yes(client, update):
    user_id = update.from_user.id
    await db.set_session(user_id, "")
    await db.set_login(user_id,False)
    await update.message.edit_text(
            text='Logged Out Successfully ✅\n\nDo terminate the login session manually')
