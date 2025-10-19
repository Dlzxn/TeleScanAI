import re

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state


from src.keyboard.inline_keyboard import keyboard

from src.states.state import FSMChannelOrText


parse_channels_router = Router(name=__name__)


@parse_channels_router.message(Command('parse'), StateFilter(default_state))
async def handler_parse_message(message: Message, state: FSMContext):
    """Обработчик реагирующий на команду parse

    Args:
        message (Message):
        state (FSMContext):
    
    Return: None
    """

    await message.answer('Отправьте мне пожалуйста либо текст поста, либо ссылку на чат')
    await state.set_state(FSMChannelOrText.data_from_the_user)


@parse_channels_router.message(StateFilter(FSMChannelOrText.data_from_the_user), F.text)
async def handler_data_from_the_user(message: Message, state: FSMContext):
    if re.match(r'(t.me)|(@)', message.text):
        await message.answer('Вы передали телеграм канал/чат. Сейчас будет парсинг. Надо выбрать', reply_markup=keyboard)
    else:
        await message.answer('Вы передали текст. Сразу Передам данные через RabbitMQ')

    await state.clear()