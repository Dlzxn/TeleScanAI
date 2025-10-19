from aiogram.fsm.state import default_state, State, StatesGroup


class FSMChannelOrText(StatesGroup):
    data_from_the_user = State()
    channel = State()
    text = State()


