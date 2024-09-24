from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.NYTimes import *

chatMessagesRouter = Router()

@chatMessagesRouter.message(CommandStart())
async def cmdStart(message: Message):
    NYTimes().get('home.json')
    await message.answer('Starting a message by /start using a filter CommandStart()')

@chatMessagesRouter.message(Command('start_2'))
async def cmdStart2(message: Message):
    await message.answer('Starting a message on /start_2 command using a filter Command()')
