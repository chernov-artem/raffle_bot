from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import *
from aiogram.types import ReplyKeyboardRemove

class FSM_goods(StatesGroup):
    good = State()

async def commands_start(message : types.Message):
    "функция старта"
    try:
        await bot.send_message(message.from_user.id, 'Готов к работе', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботов в ЛС.")

async def cm_start(message : types.Message):
    "функция старта машины состояний"
    await bot.send_message(message.from_user.id, "функция работает")
    await FSM_goods.good.set()

async def load_good(message: types.Message, state: FSMContext):
    "функция загружает новый товар по ссылке"
    async with state.proxy() as data:
        data['good'] = message.text
    await message.reply("загружаю товар " + data["good"])
    new_good = data['good']
    print(new_good)
    await bot.send_message(message.from_user.id, 'новый товар доступен')
    await state.finish()

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Загрузить'])
    dp.register_message_handler(load_good, state=FSM_goods.good)


