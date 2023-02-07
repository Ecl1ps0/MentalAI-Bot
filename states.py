from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    first_question = State()
    second_question = State()
    third_question = State()
