# Main file to start bot
import asyncio

from bot.createBot import bot, dp
from bot.handlers.commandsRouterHandler import mainCommandsRouter
from bot.handlers.callbackRouterHandler import callbackRouter
from bot.keyboards.setMenu import setMainMenu


class Bot():
    async def main(self):
        await setMainMenu(bot)

        # Include routers
        for router in [mainCommandsRouter, callbackRouter]:
            dp.include_router(router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
        
        
if __name__ == "__main__":
    asyncio.run(Bot().main())
