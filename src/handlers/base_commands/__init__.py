from aiogram import Router
from src.handlers.base_commands.base_commands import base_commands_router


base_commands_main_router = Router(name=__name__)


base_commands_main_router.include_router(base_commands_router)