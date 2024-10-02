from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *


mainCommandsRouter = Router()

@mainCommandsRouter.message(CommandStart())
async def cmdStart(message: Message):
    await message.answer(
        text='News Bot'
    )

@mainCommandsRouter.message(Command('get_news'))
async def cmdGetNews(message: Message):

    newsArray = News().sendMessage()
    await message.answer(
        text='<code>New York Times</code> top news',
        reply_markup=newsArray
    )
