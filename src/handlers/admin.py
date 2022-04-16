from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp



class FSMAdmin(StatesGroup):

    photo = State()
    name = State()
    description = State()
    price = State()


# Начало диалога загрузки нового пункта меню:
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузите фото!')

# Ловим первый ответ и пишем в словарь:
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Введите название!')

# Ловим второй ответ:
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите описание!')

# Ловим третий ответ:
#@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Теперь укажите цену!')

# Ловим последний ответ и используем полученные данные:
#@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)

    async with state.proxy as data:
        await message.reply(str(data))

    await state.finish()


# Регистрируем хендлеры:
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)