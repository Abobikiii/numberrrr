from telebot import TeleBot, types
import json
import pickle
from random import choice
import time

# t.me/t3004_bot
TOKEN = '7198013375:AAFpKLUEiEWDsELNV7ygDBBeTephI2QqyvI'
bot = TeleBot(TOKEN)
from telebot import TeleBot, types
import time

with open('bad_words.txt', 'r', encoding = 'UTF-8') as words:
    bad_words = []
    for word in words.readlines():
        bad_words.append(word.strip().lower())
    print(bad_words)

ban_time = 20 # seconds

def check_b_words(text):
    is_bun = False
    user_words = text.split(' ')
    for word in user_words:
        if word.lower() in bad_words: is_bun = True
    return is_bun 

@bot.message_handler()
def get_message(message):
    is_bun = check_b_words(message.text)
    print(is_bun)
    if is_bun:
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        send_text = first_name + ' ' + last_name + ' ЗАБАНЕН на ' + str(ban_time) + ' секунд!'
        bot.send_message(message.chat.id, text=send_text, reply_to_message_id=message.message_id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=time.time()+ban_time)
    else:
        bot.send_message(message.chat.id, text = 'OK')


if __name__ == '__main__':
    bot.polling(non_stop=True)



