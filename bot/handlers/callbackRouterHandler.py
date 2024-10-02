from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *


callbackRouter = Router()

@callbackRouter.callback_query()
async def callback_handle(call: types.CallbackQuery):
    button = call.data
    print(button)
    #await call.answer()