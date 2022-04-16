from aiogram.utils import executor

from create_bot import dp



# await message.answer(message.text) # простой ответ бота
# await message.reply(message.text) # ответ бота с цитированием
# await bot.send_message(message.from_user.id, message.text) # ответ бота личным сообщением


async def on_startup(_):
    print('Бот вышел в онлайн')


from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)