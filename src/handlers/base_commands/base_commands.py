from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command


base_commands_router = Router(name=__name__)


@base_commands_router.message(CommandStart())
async def handler_start_message(message: Message):
    """Обработчик команды /start

    Args:
        message (Message): получаемые сообщение
    
    Return:
        None
    """    
    ...


@base_commands_router.message(Command('help'))
async def handler_help_message(message: Message):
    """Обработчик команды /help

    Args:
        message (Message): получаемое сообщение
    Return:
        None
    """ 
    ...