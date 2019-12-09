import telebot
from telebot import types
from telebot import apihelper
import keyboards
import config

bot = telebot.TeleBot(config.TOKEN)
#apihelper.proxy = {'https':config.PROXY}

# test commit for
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет, я проведу тебе маленький гайд по миру скидок!',
                     reply_markup=keyboards.keyboard_main())


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Look at bot keyboard, doode!', reply_markup=keyboards.keyboard_main())


@bot.message_handler(commands=['asos'])
def asos_parser(message):
    bot.send_message(message.chat.id, 'asos', reply_markup=keyboards.keyboard_asos())


@bot.message_handler(content_types=['text'])
def main_branch(message):
    chat_id = message.chat.id
    # to main
    if message.text == 'Назад':
        bot.send_message(chat_id, 'Смотри какие магазины открыты для просмотра!', reply_markup=keyboards.keyboard_main())

    # main menu
    elif message.text == 'Обратная связь':
        bot.send_message(chat_id, 'Отложим дела и поговорим?', reply_markup=keyboards.keyboard_callback())


if __name__ == "__main__":
    bot.polling(none_stop=True)
