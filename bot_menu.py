from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#apihelper.proxy = {'https':config.PROXY}

# test commit for
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nДавай я тебе покажу мир скидок!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши команду ""/help""")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)
