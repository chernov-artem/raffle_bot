from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton('/start')
button2 = KeyboardButton('/all_contests')
button3 = KeyboardButton('/new_contest')
button4 = KeyboardButton('/channels')
button5 = KeyboardButton('/support')
button6 = KeyboardButton('/pay')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button1, button2, button3, button4, button5, button6)
kb_client2.add(button1, button2, button3, button4, button5, button6)