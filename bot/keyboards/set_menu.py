from aiogram import Bot
from aiogram.types import BotCommand

COMMANDS_RU: dict[str, str] = {
    '/start'      : 'Начать работу бота',
    '/choose_api' : 'Выберите новостной источник',
    '/get_news'   : 'Получить новости'
}

async def setMainMenu(bot: Bot):
    """
        Function for customizing the Menu button of the bot
    """

    mainMenuCommands = [
        BotCommand(
            command = command,
            description = description
        ) for command, description in COMMANDS_RU.items()
    ]

    await bot.set_my_commands(mainMenuCommands)
