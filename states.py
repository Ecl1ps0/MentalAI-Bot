from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    choose_option = State()
    first_option = State()
    second_option = State()
    third_option = State()

    first_question = State()
    second_question = State()
    third_question = State()
