from aiogram import Bot, executor, Dispatcher, types
import config
import db

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['shopping', 'start'])
async def get_id(message: types.Message):
    us = db.get_tasks()
    msg = ''
    for i in range(0, len(us), 3):
        msg = f'{msg}\n{us[i]}  ● {us[i + 1]}, id: <code>{us[i+2]}</code>'

    await message.answer(msg, parse_mode='HTML')


@dp.message_handler(commands=['add'])
async def add_task(message: types.Message):
    task = message.text[5:]
    db.create_task(task=task, username=message.from_user.first_name)
    await message.answer(f'{task}✅')


@dp.message_handler(content_types=['text'])
async def get_id(message: types.Message):
    try:
        if db.remove_task(id=int(message.text)):
            await message.answer('ok!🛒')
        else:
            await message.answer('hmm..')
    except ValueError:
        pass


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=False)
