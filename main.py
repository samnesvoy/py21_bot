from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.environ['token']
print(TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# users = ['109898386', '846624516', '581069221', '656749147', '384885336']
users = {}


@dp.message_handler()
async def echo(message: types.Message):
    print(message.from_user.id, ' - ', message.from_user.first_name, ' - ', message.text)
    users.update({message.from_user.id: message.from_user.first_name})
    # await message.answer(message.text)
    # await message.reply(message.text)
    text = f'Пользователь {message.from_user.first_name} написал {message.text}'
    for i in users.keys():
        if i != message.from_user.id:
            await bot.send_message(chat_id=i,
                                   text=text)


if __name__ == '__main__':
    executor.start_polling(dp)
