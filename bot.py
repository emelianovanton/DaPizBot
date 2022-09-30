import telebot
import re
import os

from random import randint
from time import sleep

TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)  # YOUR BOT TOKEN SHOULD BE HERE


@bot.message_handler(content_types=['text'])
def da_pizda_replies(message):
    text_message = re.sub(r'[^А-Яа-я]', '', message.text)
    sleep(randint(1, 5))
    if str.lower(text_message) == 'да':
        bot.reply_to(message, "Пизда!")
    elif str.lower(text_message) == 'пизда':
        bot.reply_to(message, "Да!")
    else:
        pass


bot.polling(none_stop=True, interval=0)
