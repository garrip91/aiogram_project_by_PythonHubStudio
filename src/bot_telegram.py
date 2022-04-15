from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from config import TOKEN, ADMIN



# await message.answer(message.text) # простой ответ бота
# await message.reply(message.text) # ответ бота с цитированием
# await bot.send_message(message.from_user.id, message.text) # ответ бота личным сообщением


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')

'''**************************************************************** КЛИЕНТСКАЯ ЧАСТЬ - НАЧАЛО ****************************************************************'''
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!') # ответ бота личным сообщением
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/garrip91_bot') # ответ бота с цитированием

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00') # ответ бота личным сообщением

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная, 15') # ответ бота личным сообщением
'''**************************************************************** КЛИЕНТСКАЯ ЧАСТЬ - КОНЕЦ *****************************************************************'''

'''***************************************************************** АДМИНСКАЯ ЧАСТЬ ****************************************************************'''

'''******************************************************************* ОБЩАЯ ЧАСТЬ ******************************************************************'''


@dp.message_handler()
async def echo_send(message: types.Message):



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)