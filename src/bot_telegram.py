from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
from config import TOKEN, ADMIN



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text) # простой ответ бота
    # await message.reply(message.text) # ответ бота с цитированием
    # await bot.send_message(message.from_user.id, message.text)) # ответ бота личным сообщением
    if message.text == 'Привет':
        await message.answer('И тебе привет!') # простой ответ бота


executor.start_polling(dp, skip_updates=True)