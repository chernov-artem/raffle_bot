from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('/кнопка1')
button2 = KeyboardButton('/кнопка2')
button3 = KeyboardButton('/кнопка3')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button1, button2, button3)