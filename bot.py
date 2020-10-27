# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
import telebot
import config
import random
from telebot import types


MESSAGE = "😊Приветствую, {0.first_name}!\nЯ - <b>{1.first_name}</b>, \nБот🤖, \
 который дарит бесплатные промокоды на различные платные сервисы \
 🤑\nВыбери в меню сервис на который хочешь получить бесплатные ништяки."


MSG_GLOVO = "[StackOverflow на русском](https://ru.stackoverflow.com/)"


MSG_KASPI = "Учи питон, а то ты даже не понимаешь основные конструкции \
            начни с этого https://www.youtube.com/watch?v=VXYyJX5qMiQ&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR"


MSG_VK = "https://vk.com"


#Стикер приветствия
STATIC_FILES = open('static/AnimatedSticker.tgs', 'rb')

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, STATIC_FILES)
    # keyboard Наша клавиатура перечисляем в строчку 
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Promo.Glovo")
    item2 = types.KeyboardButton("🎲Promo.Kaspi")
    item3 = types.KeyboardButton("🎲Promo.VK")
    markup.add(item1,item2,item3)
    #приветствие в чате в начале
    bot.send_message(message.chat.id,
                     MESSAGE.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


# назначаяем кажду кнопку  методами 
@bot.message_handler(content_types=['text'])
def cont(message):

    if message.text == '🎲Promo.Glovo':
        bot.send_message(message.chat.id, MSG_GLOVO,
        	parse_mode='Markdown')

    elif message.text == '🎲Promo.Kaspi':
        bot.send_message(message.chat.id, MSG_KASPI,
        	parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, MSG_VK,
        	parse_mode='Markdown')


if __name__ == '__main__':
    #run
    bot.polling(none_stop=True)