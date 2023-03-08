import random

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import Command
from aiogram.types import Message


from config import token
from game1 import answers

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Создаем асинхронную функцию
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/game',
                   description='игра'),
        BotCommand(command='/prediction',
                   description='предсказание')
    ]

    await bot.set_my_commands(main_menu_commands)


@dp.message(Command(commands=["game"]))
async def process_start_command(message: Message):
    await message.answer('Задай вопрос, нажми /prediction , получи ответ')

@dp.message(Command(commands=["prediction"]))
async def process_start_command(message: Message):
    await message.answer(random.choice(answers))




if __name__ == '__main__':

    dp.startup.register(set_main_menu)

    dp.run_polling(bot)
