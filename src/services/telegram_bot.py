from aiogram import Bot

from src.core.app import dispatcher
from src.config.config import Config, load_config


conf: Config = load_config()


async def run_telegram_bot():
    bot = Bot(conf.telegram_bot.token)
    await dispatcher.start_polling(bot)