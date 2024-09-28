# Main file to start bot
import asyncio

from bot.create_bot import bot, dp
from bot.handlers.chatMessages import chatMessagesRouter
from bot.keyboards.set_menu import setMainMenu


class Bot():
    async def main(self):
        await setMainMenu(bot)
        dp.include_router(chatMessagesRouter)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        
        
if __name__ == "__main__":
    asyncio.run(Bot().main())
