#Обработчик команд

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message,ReplyKeyboardRemove
from telebot import types
TOKEN = "6555005944:AAF2jQFN2DCbwE3EjXjNzUAB5TMewTIB_YU"
bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"💫Привет, {message.from_user.first_name}, меня зовут {bot.get_my_name().name}.💫"
                                      f"\n⚡️Ты попал в бот-квест!⚡️"
                                      f"\n❗️Чтобы подробнее ознакомиться с ботом, напиши /help.❗️")
    with open("media/start_picture.jpg", "rb") as f:
        bot.send_photo(message.chat.id, f)


markup = ReplyKeyboardMarkup(resize_keyboard=True)

@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, f"🌞Доброго врмени суток🌚"
                                      f"\n💫Сегодня ты можешь пройти невероятно интересный квест, созданный по мотивам фильма \"Побег из шоушенка\", но с небольшими доработками💫."
                                      f"\n💥Суть заключается в том, что ты должен совершать верные решения от которых зависит твоя жизнь💥."
                                      f"\n🚨Малейший неверный ход и тебя опять закинут за решетку🚨. "
                                      f"\n🤫Будь осторожен и внимателен🤫"
                                      f"\nЕсли готов к прохождению жми \"Поехали\"", reply_markup=markup)
markup.add(KeyboardButton("Поехали💨"))


@bot.message_handler(content_types=["text"])


def handle_questions_1_1_location(message: Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if message.text == "Поехали💨":
        bot.send_message(message.chat.id, "Тебя ховут Энди Дюфрейн, и тебе впояли два пожизненных срока за двойное убийство,"
                                          " но сам ты толком не помнишь убивал ли ты или нет, так как был пьян..."
                                          " Попав в тюрьму ты задумываешься о том, бежать или не бежать?"
                                          " Это и есть твоя первая задача, но тут еще появилась загвоздка,"
                                          " если я хочу сбежать, то как мне это сделать, побыстрее или сбежать через время разработав план..."
                                          " Это и есть твоя первая задача...")
"""
        markup.add(KeyboardButton('Бежать как можно быстрее.'))
        markup.add(KeyboardButton('Сбежать через время, продумав план.'))
        markup.add(KeyboardButton('Остаться в тюрьме отбывать два пожизненных заключения.'))


        location1_1_1question = types.KeyboardButton("Бежать как можно быстрее.")
        location1_1_2question = types.KeyboardButton("Сбежать через время, продумав план.")
        location1_1_3question = types.KeyboardButton("Остаться в тюрьме отбывать два пожизненных заключения.")
        markup.add(location1_1_1question, location1_1_2question, location1_1_3question)
"""






















bot.polling()