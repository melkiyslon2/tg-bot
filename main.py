import telebot
from telebot import types
import random
import os

bot = telebot.TeleBot("1735353527:AAH90HPaLh8HOztWPFuT21lTbPPv2jF3MtE")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1=types.KeyboardButton("Фото")
    btn2 = types.KeyboardButton("Видео")
    markup.add(btn1,btn2)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>!\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "начать заново":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1 = types.KeyboardButton("Фото")
        btn2 = types.KeyboardButton("Видео")
        markup.add(btn1,btn2)
        final_message = "Надоела эта категоория?"
    elif get_message_bot == "фото":
        """all_files_in_directory = os.listdir('D://Study//mems//photo//random')
        file = random.choice(all_files_in_directory)
        doc = open('D://Study//mems//photo//random' + '/' + file, 'rb')
        # если нужно подпись к фото
        caption = "любой текст"
        # send_random_photo
        bot.send_photo(message.chat.id, doc, caption)"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1 = types.KeyboardButton("java")
        btn2 = types.KeyboardButton("python")
        markup.add(btn1,btn2)
        final_message = "u're welcome"
    elif get_message_bot == "видео":
        """all_files_in_directory = os.listdir('D://Study//mems//video//fleks')
        file = random.choice(all_files_in_directory)
        doc = open('D://Study//mems//video//fleks' + '/' + file, 'rb')
        # если нужно подпись к фото
        caption = "любой текст"
        # send_random_photo
        bot.send_video(message.chat.id, doc)"""
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1 = types.KeyboardButton("флекс")
        btn2 = types.KeyboardButton("разное")
        markup.add(btn1,btn2)
        final_message = "приятного просмотра"
    elif get_message_bot == "python":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("фото")
        btn2 = types.KeyboardButton("видео")
        markup.add(btn1, btn2)
        final_message = "Должно быть смешно"
        all_files_in_directory = os.listdir('mems//photo//python')
        file = random.choice(all_files_in_directory)
        doc = open('mems//photo//python' + '/' + file, 'rb')
        # если нужно подпись к фото
        caption = "любой текст"
        # send_random_photo
        bot.send_photo(message.chat.id, doc)
    elif get_message_bot == "java":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("фото")
        btn2 = types.KeyboardButton("видео")
        markup.add(btn1, btn2)
        final_message = "Должно быть смешно"
        all_files_in_directory = os.listdir('mems//photo//java')
        file = random.choice(all_files_in_directory)
        doc = open('mems//photo//java' + '/' + file, 'rb')
        caption = "любой текст"
        bot.send_photo(message.chat.id, doc)
    elif get_message_bot == "флекс":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("фото")
        btn2 = types.KeyboardButton("видео")
        markup.add(btn1, btn2)
        final_message = "Должно быть смешно"
        all_files_in_directory = os.listdir('mems//video//fleks')
        file = random.choice(all_files_in_directory)
        doc = open('mems//video//fleks' + '/' + file, 'rb')
        # если нужно подпись к фото
        caption = "любой текст"
        # send_random_photo
        bot.send_video(message.chat.id, doc)
    elif get_message_bot == "разное":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("фото")
        btn2 = types.KeyboardButton("видео")
        markup.add(btn1, btn2)
        final_message = "Должно быть смешно"
        all_files_in_directory = os.listdir('mems//video//raznoe')
        file = random.choice(all_files_in_directory)
        doc = open('mems//video//raznoe' + '/' + file, 'rb')
        # если нужно подпись к фото
        caption = "любой текст"
        # send_random_photo
        bot.send_video(message.chat.id, doc)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1 = types.KeyboardButton("Фото")
        btn2 = types.KeyboardButton("Видео")
        markup.add(btn1,btn2)
        final_message = "Не найдено!"

    bot.send_message(message.chat.id,final_message,parse_mode="html",reply_markup=markup)


bot.polling(none_stop=True)

