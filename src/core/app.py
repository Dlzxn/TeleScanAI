from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.handlers import handler_router


memory_storage = MemoryStorage()


dispatcher = Dispatcher(storage=memory_storage)
dispatcher.include_router(handler_router)