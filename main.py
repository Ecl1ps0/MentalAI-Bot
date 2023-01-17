from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("5730082173:AAEZs2nXmIDDDyIZjX_mhHmhCjLekCzOVTI")


@bot.message_handler(commands=['start'])
def say_hello(message: Message):
    bot.reply_to(message, "Hi man!")


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
