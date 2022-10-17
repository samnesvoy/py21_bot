from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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
import main

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


def inline_keyboard():
    v = {'name': 'petrucho', 'age': 13}
    btn = InlineKeyboardButton(text='Кнопка', callback_data='button')
    btn1 = InlineKeyboardButton(text='Кнопка1', callback_data='button1')
    btn2 = InlineKeyboardButton(text='Кнопка2', callback_data='button2')
    btn3 = InlineKeyboardButton(text='Кнопка3', callback_data='button3')
    btn4 = InlineKeyboardButton(text='Кнопка4', callback_data='button4')
    btn5 = InlineKeyboardButton(text='Кнопка5', callback_data=str(v))
    btn6 = InlineKeyboardButton(text='Кнопка6', callback_data='button6')
    kbrd = InlineKeyboardMarkup().add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
    return kbrd


def kbrd_cat():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Category 1'),
        KeyboardButton('Category 2'))
    return menu


def kbrd_subcat():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Subcategory 1'),
        KeyboardButton('Subcategory 2'))
    return menu


def kbrd_prod():
    menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    menu.row(
        KeyboardButton('Product 1'),
        KeyboardButton('Product 2'))
    return menu


def calc():
    menu = ReplyKeyboardMarkup(resize_keyboard=True)
    menu.row(
        KeyboardButton('X'),
        KeyboardButton('Operation'),
        KeyboardButton('Y'),
    )
    return menu

# def calc(data: dict):
#     menu = ReplyKeyboardMarkup(resize_keyboard=True)
#     menu.row(
#         KeyboardButton(data['x']),
#         KeyboardButton(data['op']),
#         KeyboardButton(data['y']),
#     )
#     return menu
