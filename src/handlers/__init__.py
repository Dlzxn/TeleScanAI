from aiogram import Router
from src.handlers.base_commands import base_commands_main_router
from src.handlers.user_commands import user_commands_main_router


handler_router = Router(name=__name__)


handler_router.include_routers(
    base_commands_main_router,
    user_commands_main_router
)