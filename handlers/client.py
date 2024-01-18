from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_kb import *
from aiogram.types import ReplyKeyboardRemove

class FSM_goods(StatesGroup):
    good = State()
    step1 = State()
    step2 = State()
    step3 = State()

async def commands_start(message : types.Message):
    "функция старта"
    try:
        await bot.send_message(message.from_user.id, 'Привет! !! !', reply_markup=kb_client2)
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


async def step1(message: types.Message, state: FSM_goods):
    'функция шага 1'
    await bot.send_message((message.from_user.id, 'шаг1 '))
    await FSM_goods.step2
    await message.reply('дальше ->')

async def step2(message: types.Message, state: FSM_goods):
    'функция шага 1'
    await bot.send_message((message.from_user.id, 'шаг2 '))
    await FSM_goods.next()
    await message.reply('дальше ->')

async def step3(message: types.Message, state: FSM_goods):
    'функция шага 1'
    await bot.send_message((message.from_user.id, 'шаг3 '))
    await FSM_goods.next()
    await message.reply('дальше ->')




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
    dp.register_message_handler(cm_start, commands=['Загрузить'])
    dp.register_message_handler(load_good, state=FSM_goods.good)
    dp.register_message_handler(step1, state=FSM_goods.good)
    dp.register_message_handler(step2, state=FSM_goods.good)
    dp.register_message_handler(step3, state=FSM_goods.good)


