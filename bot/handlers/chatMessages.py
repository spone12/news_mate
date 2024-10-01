from aiogram import Router, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from bot.news.news import *
from bot.keyboards.inline import *


chatMessagesRouter = Router()

@chatMessagesRouter.message(CommandStart())
async def cmdStart(message: Message):

    keyboard = InlineKeyboard()
    
    LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',}

    BUTTONS: dict[str, str] = {
        'btn_1': '1',
        'btn_2': '2',
        'btn_3': '3',
        'btn_4': '4',
        'btn_5': '5',}

    keyboard = keyboard.create_inline_kb(2, LEXICON, BUTTONS)
    
    await message.answer(
        text='Inline keyboard '
             '<code>create_inline_kb</code>',
        reply_markup=keyboard
    )

@chatMessagesRouter.message(Command('get_news'))
async def cmdGetNews(message: Message):

    newsArray = News().sendMessage()
    for news in newsArray:
        await message.answer(news)

@chatMessagesRouter.callback_query()
async def callback_handle(call: types.CallbackQuery):
    print(call)
    #await call.answer()