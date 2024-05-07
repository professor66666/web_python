from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6520417511:AAFbUjeH_6ISOzrguMISV25dZzMX62MPKoc')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб-страницу Технум', web_app=WebAppInfo(url='https://vr-technum64.ru/')))
    markup.add(types.KeyboardButton('Открыть веб-страницу Сектор', web_app=WebAppInfo(url='https://sector64.ru/')))
    await message.answer('halo ept', reply_markup=markup)


executor.start_polling(dp)
#bot = telebot.TeleBot('6520417511:AAFbUjeH_6ISOzrguMISV25dZzMX62MPKoc')
#bot.polling(none_stop=True)


# git
