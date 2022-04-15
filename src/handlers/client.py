from aiogram import types, Dispatcher

from create_bot import dp, bot



# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!') # ответ бота личным сообщением
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/garrip91_bot') # ответ бота с цитированием

# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 09:00 до 20:00, Пт-Сб с 10:00 до 23:00') # ответ бота личным сообщением

# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Колбасная, 15') # ответ бота личным сообщением

# @dp.message_handler(commands=['Меню'])
# async def pizza_menu_command(message: types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], F'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])