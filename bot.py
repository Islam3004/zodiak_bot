import telebot
from telebot import types
from config import TOKEN
from service import get_information


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width = 2)
    btn1 = types.KeyboardButton('Меню')
    btn2 = types.KeyboardButton('Выйти')
    markup.add(btn1, btn2)
    text = "Выбери дальнейшие действие"
    bot.send_message(message.chat.id, text, reply_markup = markup)

@bot.message_handler(content_types = ['text'])
def echo(message):
    get_message = message.text
    if get_message.lower() == 'меню':
        text = 'Кликни на свой знак задиака, чтоб я тебя развёл на деньги'
        markup = types.InlineKeyboardMarkup(row_width = 12)
        item1 = types.InlineKeyboardButton('Овен', callback_data = 'oven')
        item2 = types.InlineKeyboardButton('Телец', callback_data = 'telec')
        item3 = types.InlineKeyboardButton('Близнецы', callback_data = 'bliznecy')
        item4 = types.InlineKeyboardButton('Рак', callback_data = 'rak')
        item5 = types.InlineKeyboardButton('Лев', callback_data = 'lev')
        item6 = types.InlineKeyboardButton('Дева', callback_data = 'deva')
        item7 = types.InlineKeyboardButton('Весы', callback_data = 'vesy')
        item8 = types.InlineKeyboardButton('Скорпион', callback_data = 'scorpion')
        item9 = types.InlineKeyboardButton('Стрелец', callback_data = 'strelec')
        item10 = types.InlineKeyboardButton('Козерог', callback_data = 'kozerog')
        item11 = types.InlineKeyboardButton('Водолей', callback_data = 'vodolei')
        item12 = types.InlineKeyboardButton('Рыбы', callback_data = 'ryby')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, text, reply_markup = markup)
    elif get_message.lower() == 'выйти':
        text = 'Ниrytqv мыод    !'
        bot.send_message(message.chat.id, text)

@bot.callback_query_handler(func =lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'oven':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
        elif call.data == 'telec':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text, message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'bliznecy':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'rak':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'lev':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'deva':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'vesy':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'scorpion':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'strelec':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'kozerog':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'vodolei':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

        elif call.data == 'ryby':
            data = get_information(call.data)
            text = data
            bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)

bot.polling(none_stop=True)























































# import requests
# import json 

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
 
#     send_message = "Кеттик общение"
#     bot.send_message(message.chat.id, send_message)


# @bot.message_handler(content_types=['text'])
# def echo(message):
#     get_message = message.text
#     if get_message == "Привет":
#         text = ''
#         bot.send_message(message.chat.id, text)

# bot.polling(none_stop=True)

