from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *

chatMessagesRouter = Router()

@chatMessagesRouter.message(CommandStart())
async def cmdStart(message: Message):
    await message.answer('Starting a message')

@chatMessagesRouter.message(Command('get_news'))
async def cmdGetNews(message: Message):

    newsArray = News().sendMessage()
    for news in newsArray:
        await message.answer(news)
