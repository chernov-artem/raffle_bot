from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

with open('token.txt', 'r') as file:
    token = file.read()

bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)