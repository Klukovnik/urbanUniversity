from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import logging

api = '7424534324:AAG5sfttbq6RunvNoz5KK0fsNye0iCvGhkM'
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

logging.basicConfig(level = logging.INFO)

@dp.message_handler(commands = ['start'])
async def start_message(message):
    print('Привет! Я бот, помогающий твоему здоровью.')

@dp.message_handler()
async def all(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)