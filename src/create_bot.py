from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config import TOKEN, ADMIN



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)