from aiogram import Dispatcher
from src.handlers import handler_router


dispatcher = Dispatcher()
dispatcher.include_router(handler_router)