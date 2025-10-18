from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart,Command


base_commands_router = Router(name=__name__)