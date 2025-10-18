import os

from dotenv import load_dotenv
from dataclasses import dataclass


load_dotenv()


@dataclass
class TelegramBot:
    token: str
    api_id: str
    api_hash: str
    session_name: str


@dataclass
class Config:
    telegram_bot: TelegramBot


def load_config() -> Config:

    telegram_bot = TelegramBot(
        token=os.getenv('TOKEN'),
        api_id=os.getenv('API_ID'),
        api_hash=os.getenv('API_HASH'),
        session_name=os.getenv('SESSION_NAME')
    )

    return Config(telegram_bot=telegram_bot)