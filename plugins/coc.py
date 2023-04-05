#@Ryu_god

import random
from pyrogram import *
from timi import bot


@bot.on_message(filters.command("rps"))
def play_rps(_, msg):
    user_choice = msg.text.split()[-1].lower()
    options = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(options)
    
    if user_choice == bot_choice:
        result = f"Both chose {user_choice}, it's a tie!"
    elif user_choice == 'rock':
        result = f"{bot_choice.title()} beats {user_choice}, you lose!"
    elif user_choice == 'paper':
        result = f"{user_choice.title()} beats {bot_choice}, you win!"
    elif user_choice == 'scissors':
        result = f"{bot_choice.title()} beats {user_choice}, you lose!"
    else:
        result = "Invalid choice! Please choose rock, paper, or scissors."
    
    msg.reply_text(result)



