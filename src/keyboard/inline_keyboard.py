from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


button_current_day = InlineKeyboardButton(text='Конкретный день', callback_data='button1')
button_date_range = InlineKeyboardButton(text='Диапозон дат', callback_data='button2')
button_from_date_to_present = InlineKeyboardButton(text='С даты по настоящее время', callback_data='button3')
button_all_messages = InlineKeyboardButton(text='Все сообщения', callback_data='button4')


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [button_current_day],
        [button_date_range],
        [button_from_date_to_present],
        [button_all_messages]
    ]
)