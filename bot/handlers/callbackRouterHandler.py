from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

callbackRouter = Router()

@callbackRouter.callback_query(F.data.startswith('section_'))
async def getNewsHandle(call: types.CallbackQuery):
    """
        Handle: get news on the selected topic
    """
    
    section = call.data.split('_')[1]
    news = News().getNews(section)

    await call.message.answer(
        text=news,
        show_alert=False,
        parse_mode=ParseMode.HTML
    )

@callbackRouter.callback_query(F.data.startswith('source_'))
async def setNewsSourceHandle(call: types.CallbackQuery, state: FSMContext):
    """
        Handle: Set up a news source
    """
    
    print(call.data)
    