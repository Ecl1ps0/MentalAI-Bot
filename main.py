from telebot import TeleBot
from telebot.types import Message

bot = TeleBot("5730082173:AAEZs2nXmIDDDyIZjX_mhHmhCjLekCzOVTI")


@bot.message_handler(commands=['start'])
def say_hello(message: Message):
    bot.send_message(message.chat.id, f"Welcome dear {message.from_user.first_name}! \n" +
                     "I can establish your mood and mental state by your response on a simple question:\n" +
                     "How was your day?\n" +
                     "Don’t be afraid, you can be honest with me.\n" +
                     "\n" +
                     "I can also give you free advice based on your mood.")


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
