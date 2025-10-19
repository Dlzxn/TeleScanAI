from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command, StateFilter
from aiogram.fsm.state import default_state


base_commands_router = Router(name=__name__)


@base_commands_router.message(CommandStart(), StateFilter(default_state))
async def handler_start_message(message: Message):
    """Обработчик команды /start

    Args:
        message (Message): получаемые сообщение
    
    Return:
        None
    """    
    ...


@base_commands_router.message(Command('help'), StateFilter(default_state))
async def handler_help_message(message: Message):
    """Обработчик команды /help

    Args:
        message (Message): получаемое сообщение
    Return:
        None
    """ 
    ...