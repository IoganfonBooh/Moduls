

import telebot

TOKEN = "6241892110:AAEZR8YZVzfs7ekOa18T1Hy1cWLVLkz_QWc"

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}")

bot.polling(none_stop=True)