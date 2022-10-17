from aiogram import Bot, Dispatcher, executor, types
import os

import db
import keyboards
import keyboards as kb


TOKEN = os.environ['token']
print(TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# users = ['109898386', '846624516', '581069221', '656749147', '384885336']
users = {}


@dp.message_handler(content_types=['contact', 'location'])
async def ph(message: types.Message):
    print('--')
    print(message)


class State:
    states = [
        'основное меню',
        'ввод х',
        'ввод оператора',
        'ввод y',
    ]
    data = {
        'x': 'X',
        'y': 'Y',
        'op': 'operator',
    }
    state = ''

    def __init__(self):
        self.state = self.states[0]

    def __str__(self):
        return f'\n***\n{self.data}\n{self.state}\n***\n'


# в этом словаре в качестве ключа будет user_id из telegram, а в качестве значения - State
users = {}


@dp.message_handler()
async def calculator(message: types.Message):
    chat_id = message.from_user.id
    if users.get(chat_id) is None:
        users.update({chat_id: State()})
    if message.text == 'X':
        users[chat_id].state = State().states[1]
        text = 'Input X'
    elif message.text == 'Operation':
        users[chat_id].state = State().states[2]
        text = 'Input operator'
    elif message.text == 'Y':
        users[chat_id].state = State().states[3]
        text = 'Input Y'
    else:
        if users[chat_id].state == State().states[1]:
            users[chat_id].data['x'] = message.text
        elif users[chat_id].state == State().states[2]:
            users[chat_id].data['op'] = message.text
        elif users[chat_id].state == State().states[3]:
            users[chat_id].data['y'] = message.text
        users[chat_id].state = State().states[0]
        text = f'{users[chat_id].data["x"]} {users[chat_id].data["op"]} {users[chat_id].data["y"]}'
    await bot.send_message(chat_id, text, reply_markup=kb.calc())
    print(f'{chat_id}-{message.from_user.username}', users[chat_id])

    # @dp.message_handler()
    # async def prod_menu(message: types.Message):
    #     global state, x, y, op
    #     chat_id = message.from_user.id
    #     mes = message.text
    #     if mes == 'X':
    #         state = 'ввод х'
    #         await bot.send_message(chat_id, 'Введите Х')
    #     elif mes == 'Y':
    #         state = 'ввод y'
    #         await bot.send_message(chat_id, 'Введите Y')
    #     elif mes == 'Operation':
    #         state = 'ввод оператора'
    #         await bot.send_message(chat_id, 'Введите оператор')
    #     elif state == 'ввод х':
    #         x = mes
    #         state = 'основное меню'
    #         await bot.send_message(chat_id, f'{x} {op} {y}', reply_markup=kb.calc())
    #     elif state == 'ввод y':
    #         y = mes
    #         state = 'основное меню'
    #         await bot.send_message(chat_id, f'{x} {op} {y}', reply_markup=kb.calc())
    #     elif state == 'ввод оператора':
    #         op = mes
    #         state = 'основное меню'
    #         await bot.send_message(chat_id, f'{x} {op} {y}', reply_markup=kb.calc())
    #     else:
    #         state = 'основное меню'
    #         await bot.send_message(chat_id, 'Калькулятор', reply_markup=kb.calc())
    #     # if mes == 'Category 1':
    #     #     kbrd = kb.kbrd_subcat()
    #     #     text = "Category's"
    #     # elif mes == 'Subcategory 1':
    #     #     kbrd = kb.kbrd_prod()
    #     #     text = 'Products'
    #     # else:
    #     #     kbrd = kb.kbrd_cat()
    #     #     text = 'Main menu'
    #     # await bot.send_message(chat_id=chat_id, text=text, reply_markup=kbrd)
    #
    #
    # @dp.message_handler()
    # async def echo(message: types.Message):
    #     print(message)
    #     # print(message.from_user.id, ' - ', message.from_user.first_name, ' - ', message.text)
    #     user = {
    #         'id_telegram': message.from_user.id,
    #         'username': message.from_user.username,
    #         'name': message.from_user.first_name
    #     }
    #     if len(db.get_user(message.from_user.id)) == 0:
    #         db.add_user(user)
    #     users.update({message.from_user.id: message.from_user.first_name})
    #     # keyboard = kb.keyboard_menu
    #     if message.text == 'Инлайн клавиатура':
    #         keyboard = kb.inline_keyboard()
    #     else:
    #         keyboard = kb.get_kbrd()
    #         keyboard.add(types.KeyboardButton('Инлайн клавиатура'))
    #
    #     await message.answer(message.text, reply_markup=keyboard)
    #     await bot.send_photo(chat_id=message.from_user.id, photo=types.InputFile('img/img.jpg'))
    #     # await message.reply(message.text)
    #
    #     # text = f'Пользователь {message.from_user.first_name} написал {message.text}'
    #     # for i in users.keys():
    #     #     if i != message.from_user.id:
    #     #         await bot.send_message(chat_id=i,
    #     #                                text=text)


@dp.callback_query_handler()
async def call_echo(callback_q: types.CallbackQuery):
    print(callback_q)
    await bot.answer_callback_query(callback_q.id, text='qqqqqq')
    await bot.send_message(chat_id=callback_q.from_user.id, text=callback_q.data)


if __name__ == '__main__':
    executor.start_polling(dp)
# executor.start_polling(dp)
