#Credits To: Github.com/Kakeguri-Domain
#Devs: Github.com/Ryu120 , Github.com/Theblacklinen 
#Contact Through Telegram: Sebastiansupport 

from pyrogram import *
import os
import time
from typing import Union
from nekosbest import Client as timi, Result
import asyncio 
import requests 

Timi = timi()

"""
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("BOT_TOKEN", None)
"""
API_ID = "14676558"
API_HASH = "b3c4bc0ba6a4fc123f4d748a8cc39981"
BOT_TOKEN = "5638227558:AAFoVUIY23zXUfGpVNzPiHcaA3k_J7mIGWs"

bot = Client("Timi", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
chat = update.effective_chat
user = update.effective_user
message = update.effective_message

print('Bot is Starting. Created By https://t.me/Sebastiansupport Devs. Timi is Running ')

#My Pro Owner: @Demon_lord_adi(telegram User)

ALIVE = ["https://telegra.ph/file/e39308158586bce4b9891.jpg", "https://telegra.ph/file/e9cce8b66270a4228fba6.jpg", "https://telegra.ph/file/f08c94883a79081b84255.jpg"]

def get_command(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@TimiCuteBot"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@TimiCuteBot"])
  return filters.command(res, prefixes=["t", "T"])

@bot.on_message(filters.command('start') & filters.group)
async def timistart(_,message):
    await message.reply_text('Heyy, Watashi Wa Timi Is up')

@bot.on_message(get_command('imi') & filters.group)
async def timistart(_,message):
    await message.reply_text('Yes, Heyy! Timi is watching you *cuddles*')
    
@bot.on_message(filters.command('slap') & filters.group)
async def timistart(_,message):
    await message.reply_text('bashes him with a bat!')
    
@bot.on_message(filters.command('hug') & filters.group)
async def timistart(_,message):
    await message.reply_text('hugs you!')
    
@bot.on_message(filters.command('pin') & filters.group)
async def timistart(_,message):
   await message.pin(message.reply_text)
   await message.reply_text('msg is pinned ')
  
@bot.on_message(filters.command('ban') & filters.group)
async def timistart(_,message): 
  await chat.ban_member(user.id)
  await message.reply_text('succesfully banned ')
  
@bot.on_message(filters.command('unpinall') & filters.group)
async def timistart(_,message): 
 await chat.unpin_all_messages()
 await message.reply_text('all message unpinned ') 


@bot.on_message(filters.command('alive') & filters.group)
async def get_img(_,message):
    result = Timi.get_image("neko")
    await message.reply_animation(result)


bot.start()

print("Heyy I am up!!")
print("Timi Version = v1.0.0")
idle()
  
