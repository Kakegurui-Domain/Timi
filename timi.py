#Credits To: Github.com/Kakeguri-Domain
#Devs: Github.com/Ryu120 , Github.com/Theblacklinen, GitHub.com/SOME-1HING
#Contact Through Telegram: https://t.me/Sebastiansupport 

from pyrogram import *
from telethon import *
import os, random
import time
from typing import Union
from nekosbest import Client as timi, Result
import asyncio 
import requests 
from strings import TIMI_NEKO, TIMI_HELP
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

Timi = timi()

"""
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
TOKEN = os.environ.get("BOT_TOKEN", None)
"""
API_ID = "14676558"
API_HASH = "b3c4bc0ba6a4fc123f4d748a8cc39981"
BOT_TOKEN = "5638227558:5923067353:AAFmAiiRq7vKsA9Atxn_C_Bn66YkWlRExLQ"

bot = Client("Timi", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

TIMI = """Timi is Up....!\n • Timi version: `v1.0.0-Beta`\n • Timi loves to play"""
TIMI_MSG = """Watashi Wa Timi is up!\n •Use /help to know my commands >~<"""

Buttons = [
        [
            InlineKeyboardButton(
                "🆘", url="https://t.me/Sebastian_support"
            ),
        ]
    ]

buttons = [
        [
            InlineKeyboardButton(
                "🆘", url="https://t.me/Sebastian_latest"
            ),
            InlineKeyboardButton(
                "⚙️", url="https://t.me/Sebastian_update"
            ),
        ]
    ]

print('Bot is Starting. Created By https://t.me/Sebastiansupport Devs. Timi is Running ')

#My Pro Owner: @Demon_lord_adi(telegram User)

ALIVE = ["https://telegra.ph/file/e39308158586bce4b9891.jpg", "https://telegra.ph/file/e9cce8b66270a4228fba6.jpg", "https://telegra.ph/file/f08c94883a79081b84255.jpg"]

url_sfw = "https://api.waifu.pics/sfw/" 

def get_command(comm: Union[list, str]):
  res = list()
  if isinstance(comm, str):
    res.extend([comm, f"{comm}@TimiCuteBot"])
  if isinstance(comm, list):
    for com in comm:
      res.extend([com, f"{com}@TimiCuteBot"])
  return filters.command(res, prefixes=["t", "T"])

@bot.on_message(filters.command('start'))
async def timistart(_,message):
    Ttimi = requests.get("https://nekos.best/api/v2/neko")
    data = Ttimi.json()
    img = (data["results"][0]["url"])
    return await message.reply_photo(
      photo=img,
      caption=TIMI_MSG,
      reply_markup=InlineKeyboardMarkup(buttons)
    )

@bot.on_message(get_command('imi') & filters.group)
async def timistart(_,message):
    Hm = random.choice(TIMI_NEKO)
    await message.reply_text(Hm)
    
@bot.on_message(filters.command('alive') & filters.group)
async def get_img(_,message):
    Ttimi = requests.get("https://nekos.best/api/v2/neko")
    data = Ttimi.json()
    img = (data["results"][0]["url"])
    return await message.reply_photo(
      photo=img,
      caption=TIMI,
      reply_markup=InlineKeyboardMarkup(Buttons)
    )

@bot.on_message(filters.command('pout'))
async def pout(_, message):
    resp = requests.get("https://nekos.best/api/v2/pout")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_animation(img)

@bot.on_message(filters.command('bored'))
async def bored(_, message):
    resp = requests.get("https://nekos.best/api/v2/bored")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_animation(img)

@bot.on_message(filters.command('nekos'))
async def nekos2(_, message):
    resp = requests.get("https://nekos.best/api/v2/neko")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_photo(photo=img)

@bot.on_message(filters.command('stare'))
async def stare(_, message):
    resp = requests.get("https://nekos.best/api/v2/stare")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_animation(img)

@bot.on_message(filters.command('think'))
async def think(_, message):
    resp = requests.get("https://nekos.best/api/v2/think")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_animation(img)

@bot.on_message(filters.command('thumbsup'))
async def thumbsup(_, message):
    resp = requests.get("https://nekos.best/api/v2/thumbsup")
    data = resp.json()
    img = (data["results"][0]["url"])
    await message.reply_animation(img)


@bot.on_message(filters.command('bully'))
async def bully(_, message):
    url = f"{url_sfw}bully" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('cuddle'))
async def cuddle(_, message):
    url = f"{url_sfw}cuddle" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('cry'))
async def cry(_, message):
    url = f"{url_sfw}cry" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('hug'))
async def hug(_, message):
    url = f"{url_sfw}hug" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('awoo'))
async def awoo(_, message):
    url = f"{url_sfw}awoo" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('kiss'))
async def kiss(_, message):
    url = f"{url_sfw}kiss" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('lick'))
async def lick(_, message):
    url = f"{url_sfw}lick" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('pat'))
async def pat(_, message):
    url = f"{url_sfw}pat" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('smug'))
async def smug(_, message):
    url = f"{url_sfw}smug" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('bonk'))
async def bonk(_, message):
    url = f"{url_sfw}bonk" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('yeet'))
async def yeet(_, message):
    url = f"{url_sfw}yeet" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('blush'))
async def blush(_, message):
    url = f"{url_sfw}blush" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('smile'))
async def smile(_, message):
    url = f"{url_sfw}smile" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('wave'))
async def wave(_, message):
    url = f"{url_sfw}wave" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('highfive'))
async def highfive(_, message):
    url = f"{url_sfw}highfive" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('handhold'))
async def handhold(_, message):
    url = f"{url_sfw}handhold" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('nom'))
async def nom(_, message):
    url = f"{url_sfw}nom" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('bite'))
async def bite(_, message):
    url = f"{url_sfw}bite" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)


@bot.on_message(filters.command('glomp'))
async def glomp(_, message):
    url = f"{url_sfw}glomp" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('slap'))
async def slap(_, message):
    url = f"{url_sfw}slap" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('killgif'))
async def killgif(_, message):
    url = f"{url_sfw}kill" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('kickgif'))
async def kickgif(_, message):
    url = f"{url_sfw}kick" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('happy'))
async def happy(_, message):
    url = f"{url_sfw}happy" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('wink'))
async def wink(_, message):
    url = f"{url_sfw}wink" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('poke'))
async def poke(_, message):
    url = f"{url_sfw}poke" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('dance'))
async def dance(_, message):
    url = f"{url_sfw}dance" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)
    

@bot.on_message(filters.command('cringe'))
async def cringe(_, message):
    url = f"{url_sfw}cringe" 
    result = requests.get(url).json()
    img = result['url']
    await message.reply_animation(img)

@bot.on_message(filters.command('help'))
async def timihelp(_,message):
    await message.reply_text(TIMI_HELP)

bot.start()

print("Heyy I am up!!")
print("Timi Version = v1.0.0-Beta")
idle()
  
