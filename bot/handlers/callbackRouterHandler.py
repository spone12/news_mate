from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *
from aiogram.enums import ParseMode

callbackRouter = Router()

@callbackRouter.callback_query()
async def callback_handle(call: types.CallbackQuery):
    split = call.data.split('_')
    sectionName = News().getSectionById(int(split[1]))
    news = News().getNews(sectionName)

    await call.message.answer(
        text=news,
        show_alert=False,
        parse_mode=ParseMode.HTML
    )
    