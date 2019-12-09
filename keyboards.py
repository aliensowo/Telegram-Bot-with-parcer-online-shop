import telebot
from telebot import types
from parser_asos import s_parse


def keyboard_callback():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    btn1 = types.KeyboardButton('Помочь')
    btn2 = types.KeyboardButton('Написать отзыв')
    btn3 = types.KeyboardButton('Обо мне')
    btn4 = types.KeyboardButton('Назад')

    markup.add(btn1, btn2, btn3, btn4)

    return markup


def keyboard_main():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    btn1 = types.KeyboardButton('ASOS (рабочий)')
    btn2 = types.KeyboardButton('Lamoda (рабочий)')
    btn3 = types.KeyboardButton('WildBerries (временно не работает)')

    markup.add(btn1, btn2, btn3)

    return markup


def keyboard_asos():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('ASOS', callback_data=s_parse())

    markup.add(btn1)

    return markup
