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
        bot.send_message(callback.message.chat.id, "option1")
    elif callback == "option2":
        bot.send_message(callback.message.chat.id, "option2")
    else:
        bot.send_message(callback.message.chat.id, "option3")


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()
