# Main file to start bot
import asyncio
import sys

from bot.create_bot import bot, dp, logger
from bot.handlers.chatMessages import chatMessagesRouter

class Bot():
    async def main(self):
        dp.include_router(chatMessagesRouter)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(Bot().main())
