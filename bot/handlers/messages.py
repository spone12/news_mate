from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

messages_router = Router()

@messages_router.message(CommandStart())
async def cmdStart(message: Message):
    await message.answer('Starting a message by /start using a filter CommandStart()')

@messages_router.message(Command('start_2'))
async def cmdStart2(message: Message):
    await message.answer('Starting a message on /start_2 command using a filter Command()')
