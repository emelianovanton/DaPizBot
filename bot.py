import requests
import telebot

bot = telebot.TeleBot('')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if str.lower(message.text) == 'да':
        bot.send_message(message.from_user.id, 'пизда')
    elif str.lower(message.text) == 'пизда':
        bot.send_message(message.from_user.id, 'да')
    else:
        bot.send_message(message.from_user.id, 'умею отвечать только на "да" и "пизда"')


bot.polling(none_stop=True, interval=0)
