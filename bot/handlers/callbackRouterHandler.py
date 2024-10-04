from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

callbackRouter = Router()

@callbackRouter.callback_query(F.data.startswith('section_'))
async def callbackHandle(call: types.CallbackQuery):
    
    split = call.data.split('_')
    sectionName = News().getSectionById(int(split[1]))
    news = News().getNews(sectionName)

    await call.message.answer(
        text=news,
        show_alert=False,
        parse_mode=ParseMode.HTML
    )

@callbackRouter.callback_query(F.data.startswith('source_'))
async def setNewsSource(call: types.CallbackQuery, state: FSMContext):
    print(call.data)
    