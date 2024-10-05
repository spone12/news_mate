from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *


mainCommandsRouter = Router()

@mainCommandsRouter.message(CommandStart())
async def cmdStart(message: Message):
    """
        Command start
    """
    
    await message.answer(
        text='News Bot'
    )

@mainCommandsRouter.message(Command('get_news'))
async def cmdGetNews(message: Message):
    """
        Command the “get_news” displays a list of news category buttons
    """
    
    sectionButtonsArray = News().getSectionButtons()
    await message.answer(
        text='Choose the topic news',
        reply_markup=sectionButtonsArray
    )

@mainCommandsRouter.message(Command('news_source'))
async def cmdGetNewsSources(message: Message):
    """
        Command get news sources
    """
    
    newsSource = News().getNewsSources()
    await message.answer(
        text='Choose the news source',
        reply_markup=newsSource
    )
