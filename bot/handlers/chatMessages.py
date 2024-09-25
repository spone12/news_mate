from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.NYTimes import *

chatMessagesRouter = Router()

@chatMessagesRouter.message(CommandStart())
async def cmdStart(message: Message):
    responseData = NYTimes().get('home.json')

    # temporarily here
    for i in range(0, responseData['num_results'] - 1):
        await message.answer(responseData[i]['url'])

@chatMessagesRouter.message(Command('start_2'))
async def cmdStart2(message: Message):
    await message.answer('Starting a message on /start_2 command using a filter Command()')
