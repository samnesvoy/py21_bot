from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db import get_users

btn1 = KeyboardButton('some text')
btn2 = KeyboardButton('some text2', )
keyboard_test = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
keyboard_test.add(btn1, btn2)
keyboard_test.insert(btn1)
keyboard_test.add(btn1)
keyboard_test.row(btn1, btn2, btn1)
keyboard_test.row(btn1)
keyboard_test.add(btn1, btn1, btn2)

menu = ['pizza', 'суши', "колбаса", "торт", "еще что нибудь"]

keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
for i in menu:
    keyboard_menu.insert(i)


def get_kbrd():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for user in get_users():
        menu.insert(KeyboardButton(user[3]))
    menu.row(
        KeyboardButton('Телефон', request_contact=True),
        KeyboardButton('Где ты', request_location=True))
    return menu
