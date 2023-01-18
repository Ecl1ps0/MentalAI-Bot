import config


from telebot import TeleBot
from telebot import types
from telebot.types import Message
from states import States
from telebot import custom_filters


bot = TeleBot(config.Telegram_Token)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
option1 = types.KeyboardButton("sss")
option2 = types.KeyboardButton("aaa")
option3 = types.KeyboardButton("ddd")


@bot.message_handler(commands=['start'])
def say_hello(message: Message):
    bot.send_message(message.chat.id, f"Welcome dear {message.from_user.first_name}! \n" +
                     "I can establish your mood and mental state by your response on a simple question:\n" +
                     "How was your day?\n" +
                     "Don’t be afraid, you can be honest with me.\n" +
                     "\n" +
                     "I can also give you free advice based on your mood. \n" +
                     "Now you could see the options that we can provide.", reply_markup=markup)

    markup.add(option1, option2, option3)

    bot.set_state(message.from_user.id, States.choose_option)


@bot.message_handler(state=States.choose_option)
def chose_option_stage(message: Message):
    if message.text == option1.text:
        bot.send_message(message.chat.id, "sss")
        bot.set_state(message.from_user.id, States.first_option)
    elif message.text == option2:
        bot.send_message(message.chat.id, "aaa")
        bot.set_state(message.from_user.id, States.second_option)
    else:
        bot.send_message(message.chat.id, "ddd")
        bot.set_state(message.from_user.id, States.third_option)


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()
