
from Timi import bot
from pyrogram import*

from transformers import pipeline


timi = pipeline("text-generation", timi="gpt2")


@bot.on_message(filters.text)
def handle_message(client, message):
    response = timi(message.text, max_length=50, do_sample=True, temperature=0.7)[0]['generated_text']
    bot.send_message(message.chat.id, response)


