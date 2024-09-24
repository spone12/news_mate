# Main file to start bot
import asyncio
import logging
import sys

from create_bot import bot, dp, logger
from handlers.messages import messages_router

async def main():
    dp.include_router(messages_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
