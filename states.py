from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    ask_question = State()
