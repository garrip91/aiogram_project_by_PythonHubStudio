import environ
from config import TOKEN, ADMIN

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage


env = environ.Env(
    # set casting, default value
    ADMIN=(int, 0)
)

environ.Env.read_env()

storage = MemoryStorage()

bot = Bot(token=env('TOKEN'))
dp = Dispatcher(bot, storage=storage)