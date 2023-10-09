from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO

from config import token

basicConfig(level=INFO)
bot =Bot(token=token)
dp = Dispatcher(bot)

start_keyboard =[
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("UI/UX"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("IOS")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboard)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Привет {message.from_user.full_name}!! ",reply_markup=start_button)

@dp.message_handler(text='Backend')
async def backend(message:types.Message):
    await message.reply("""Backend — это внутренняя часть сайта и сервера и т.д
Стоимость 10000 сом в месяц
Обучение: 5 месяц""")

@dp.message_handler(text="Frontend")
async def frontend(message:types.Message):
    await message.reply("""Frontend - это  все, что браузер может читать, выводить на экран и / или запускать. То есть это HTML, CSS и JavaScript.
                    Стоимость - 14000 сом в месяц
                    Обучение - 5 месяцев""")

@dp.message_handler(text = 'Android')
async def Android(message:types.Message):
    await message.reply("""Стань Android-разработчиком с нуля за 7 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 7 месяцев""")


@dp.message_handler(text = 'IOS')
async def ios(message:types.Message):
    await message.reply("""Стань iOS-разработчиком с нуля за 7 месяцев и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 7 месяцев""")


@dp.message_handler(text = 'UI/UX')
async def UI_UX(message:types.Message):
    await message.reply("""Стань UX/UI-дизайнером с нуля за 3 месяца и получи доступ к стажировке + помощь в трудоустройстве!

Длительность: 3 месяца""")



executor.start_polling(dp)