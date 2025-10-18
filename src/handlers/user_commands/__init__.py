from aiogram import Router
from src.handlers.user_commands.parse_channels import parse_channels_router


user_commands_main_router = Router(name=__name__)


user_commands_main_router.include_routers(
    parse_channels_router   
)