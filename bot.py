import telebot
import re
import os

from random import randint
from time import sleep

TOKEN = os.environ["TOKEN"]

bot = telebot.TeleBot(TOKEN)  # YOUR BOT TOKEN SHOULD BE HERE


@bot.message_handler(content_types=['text'])
def da_pizda_replies(message):
    text_message = re.sub(r'[^А-Яа-яA-Za-z]', '', message.text)
    sleep(randint(1, 5))
    lower_text_message = str.lower(text_message)
    if lower_text_message == 'да' or lower_text_message == 'дa':
        bot.reply_to(message, "Пизда!")
    if lower_text_message == 'пизда':
        bot.reply_to(message, "Да!")
    if lower_text_message == 'нет' or lower_text_message == 'нeт':
        bot.reply_to(message, "Пидора ответ😏")

bot.polling(none_stop=True, interval=0)
