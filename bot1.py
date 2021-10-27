# import requests
# import json
# token = "2096976934:AAHt0W7a_t1OI6-ewdDZtl6856zGqPwG5uE"
# url=f"https://api.telegram.org/bot{token}/getUpdates"

# r=requests.get(url)
# # print(r.content)

# update = json.loads(r.content.decode('utf-8'))
# message = update['result'][0]
# chat_id = message['message']['chat']['id']
# url=f"https://api.telegram.org/bot{token}/sendMessage"
# # while True:
# response = requests.post(url, {"chat_id":chat_id, "text":"это был Аби"})



# import telebot
# from telebot import types
# from config import TOKEN
# from service import get_weather
# bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     btn1 = types.KeyboardButton('Меню')
#     btn2 = types.KeyboardButton('Выйти')
#     markup.add(btn1, btn2)
#     text = "Привет, я твой бот. Выбирай дальнейшие действия."
#     bot.send_message(message.chat.id, text, reply_markup=markup)



# @bot.message_handler(content_types=['text'])
# def echo(message):
#     get_message = message.text
#     if get_message.lower() == 'меню':
#         text = 'Пожалуйста выберите город температуру, которой хотите узнать'
#         markup = types.InlineKeyboardMarkup(row_width=3)
#         item1 = types.InlineKeyboardButton("Бишкек", callback_data='bishkek')
#         item2 = types.InlineKeyboardButton("Москва", callback_data='moscow')
#         item3 = types.InlineKeyboardButton("Алматы", callback_data='almaty')
#         item4 = types.InlineKeyboardButton("Получить фото", callback_data='photo')
#         item5 = types.InlineKeyboardButton("Получить музыку", callback_data='music')
#         markup.add(item1, item2, item3,item4, item5)
#         bot.send_message(message.chat.id, text, reply_markup = markup)
#     elif get_message.lower() == 'выйти':
#         text = 'Пока, рад был поговорить'
#         bot.send_message(message.chat.id, text)

# def check_temperature(temp):
#     if temp > 15:
#         return "На улице тепло , можете одеться свободно"
#     elif temp < 5: 
#         return "На улице очень холодно , следует одеть куртку"
#     elif temp < 15 and temp > 5:
#         return  "На улице холодновато , одентесь теплее"
#     else:
#         return "Неправильные данные температуру"


# #реакция нажатия на кнопки в сообщении 
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'bishkek':
#                 data = get_weather(call.data)
#                 text = f'''
#                     Температура в городе Бишкек: {data['temp_c']} \n Время в городе: {data['time']} \n {check_temperature(data['temp_c'])}
#                 '''         
#                 bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
#             elif call.data == 'moscow':
#                 data = get_weather(call.data)
#                 text = f'''
#                     Температура в городе Москва: {data['temp_c']}  \n Время в городе: {data['time']} \n {check_temperature(data['temp_c'])}
#                 '''  
#                 bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
#             elif call.data == 'almaty':
#                 data = get_weather(call.data)
#                 text = f'''
#                     Температура в городе Алматы: {data['temp_c']} \n  Время в городе: {data['time']} \n {check_temperature(data['temp_c'])}
#                 ''' 
#                 bot.edit_message_text(chat_id=call.message.chat.id, text=text,message_id=call.message.message_id, reply_markup=None)
#             elif call.data == 'photo':
#                 photo = open('photo.jpeg', 'rb')
#                 bot.send_photo(call.message.chat.id, photo)
#             elif call.data == 'music':
#                 music_file = open('Seven Nation Army (Ben Callahan remix)#[E5 M].mp3', 'rb')
#                 bot.send_audio(call.message.chat.id, music_file)
#             # remove inline buttons
#             # bot.edit_message_text(chat_id=call.message.chat.id, text='delete',message_id=call.message.message_id, reply_markup=None)
#     except Exception as e:
#         print(repr(e))
    

# bot.polling(none_stop=True)