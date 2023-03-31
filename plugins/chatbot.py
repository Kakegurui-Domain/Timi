from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Timi import bot
from pyrogram import*

Timi = ChatBot("Timibot")
Timi.set_trainer(ChatterBotCorpusTrainer)
Timi.train("chatterbot.corpus.english")

@bot.on_message(filters.text)
def reply_message(bot, update):
    user_text = update.message.text
    response = str(english_bot.get_response(user_text))
    bot.send_message(chat_id=update.message.chat_id, text=response)
