from telebot import TeleBot
from telebot import custom_filters
from telebot import types
from telebot.types import Message, CallbackQuery

import config
from states import States

bot = TeleBot(config.Telegram_Token)


def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(types.InlineKeyboardButton("option1", callback_data="option1"),
               types.InlineKeyboardButton("option2", callback_data="option2"),
               types.InlineKeyboardButton("option3", callback_data="option3"))

    return markup


@bot.message_handler(commands=['start'])
def say_hello(message: Message):
    bot.send_message(message.chat.id, f"Welcome dear {message.from_user.first_name}! \n" +
                     "I can establish your mood and mental state by your response on a simple question:\n" +
                     "How was your day?\n" +
                     "Don’t be afraid, you can be honest with me.\n" +
                     "\n" +
                     "I can also give you free advice based on your mood. \n" +
                     "Now you could see the options that we can provide.", reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda call: True)
def button_callback(callback: CallbackQuery):
    if callback.data == "option1":
        bot.send_message(callback.message.chat.id, "Let's start the questionary!")
        bot.set_state(callback.from_user.id, States.ask_question, callback.message.chat.id)
        bot.send_message(callback.message.chat.id, "Asking first question////")
    elif callback.data == "option2":
        bot.send_message(callback.message.chat.id, "option2")
    else:
        bot.send_message(callback.message.chat.id, "option3")


@bot.message_handler(state=States.ask_question)
def ask_question(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as answer:
        answer = message.text

        msg = f"Your answer is: {answer}"
        bot.send_message(message.chat.id, msg)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state="*", commands=['cancel'])
def stop_asking(message: Message):
    bot.send_message(message.chat.id, "Okay, you could start again, whenever you want.")
    bot.delete_state(message.from_user.id, message.chat.id)


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()


# @bot.message_handler(state=States.second_question)
# def second_question(message: Message):
#     bot.set_state(message.from_user.id, States.third_question, message.chat.id)
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         data['second_question_answer'] = message.text
#     bot.send_message(message.chat.id, "Asking third question////")
#
#
# @bot.message_handler(state=States.third_question)
# def third_question(message: Message):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         msg = (f"<b>First question answer: {data['first_question_answer']}\n"
#                f"Second question answer: {data['second_question_answer']}\n"
#                f"Third question answer: {message.text}</b>")
#         bot.send_message(message.chat.id, msg, parse_mode='html')
#
#     bot.delete_state(message.from_user.id, message.chat.id)
