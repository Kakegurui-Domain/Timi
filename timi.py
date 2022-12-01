#Credits To: Github.com/Kakeguri-Domain
#Devs: Github.com/Ryu120 , Github.com/Theblacklinen 
#Contact Through Telegram: Sebastiansupport 

from pyrogram import *
import os
import time

bot = Client(
    'Timi'
    api_id=API_ID,
    api_hash=API_HASH,
    token=BOT_TOKEN
)

"""
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("BOT_TOKEN", None)
"""
API_ID = "14676558"
API_HASH = "b3c4bc0ba6a4fc123f4d748a8cc39981"
BOT_TOKEN = "5638227558:AAFoVUIY23zXUfGpVNzPiHcaA3k_J7mIGWs"

print('Bot is Starting. Created By https://t.me/Sebastiansupport Devs. Timi is Running ')

#My Pro Owner: @Demon_lord_adi(telegram User)


@bot.on_message(filters.command('start') & filters.group)
async def timistart(_,message):
    await message.reply_text('Heyy, Watashi Wa Timi Is up')


bot.start()

print("Heyy I am up!!")
print("Timi Version = v1.0.0")
idle()

