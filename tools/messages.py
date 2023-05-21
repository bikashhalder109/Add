from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

START = """
━━━━━━━━━━━━━━━━━━━━━

**🥀 𝐇𝐞𝐲 {}!**

┏━━━━━━━━━━━━━━━━━┓
┣❥︎ ♕︎ 𝐎𝐰𝐧𝐞𝐫 ♕︎ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/BikashHalder)
┣❥︎ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/BikashGadgetsTech)
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/Bgt_Chat)
┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [𝐁𝐢𝐤𝐚𝐬𝐡](https://t.me/BikashHalder)
┗━━━━━━━━━━━━━━━━━┛

🥀 𝐉𝐮𝐬𝐭 𝐔𝐬𝐞 𝐌𝐞 & 𝐀𝐝𝐝 𝐌𝐞𝐦𝐛𝐞𝐫𝐬
𝐢𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 🌺

━━━━━━━━━━━━━━━━━━━━━
"""
HELP = """
🥀 𝐔𝐬𝐞 𝐁𝐞𝐥𝐨𝐰 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐓𝐨 𝐔𝐬𝐞 𝐁𝐨𝐭 🤖..

• Add one or more accounts to be able to use the bot. It is preferable to add a fake number

- After adding a number to the bot, you can transfer members from any group to your group or channel🤖✔.

**Bot Usage Commands 🤖💖**

- /start **Start The Bot**

- /login ** Log In Your Id For Add Members**

- /status **Check Status**

- /memadd **Add Members** 

- /help **For More Help**

[Join For More Updates](https://t.me/BikashGadgetsTech)

[Join For More Help Or Report](https://t.me/Bgt_Chat)
"""
# /ping **use this to check the server ping and uptime of this bot**
# - /stop for stop the adding process.
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ],[
        InlineKeyboardButton('Join Updates Channel',url = 'https://t.me/BikashGadgetsTech')],[
        InlineKeyboardButton('Join Support Group',url = 'https://t.me/Bgt_Chat'),
        ]
        ]
       
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Close', callback_data='close')
        ],[
        InlineKeyboardButton('Join Updates Channel',url = 'https://t.me/BikashGadgetsTech')],[
        InlineKeyboardButton('Join Support Group',url = 'https://t.me/Bgt_Chat'),
        ]
        ]
       
    )