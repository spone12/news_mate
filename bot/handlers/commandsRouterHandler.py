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

    sectionArray = News().getSections()
    await message.answer(
        text='Choose the topic news',
        reply_markup=sectionArray
    )

@mainCommandsRouter.message(Command('news_source'))
async def cmdGetNewsSources(message: Message):
    newsSource = News().getNewsSources()
    await message.answer(
        text='Choose the news source',
        reply_markup=newsSource
    )
