#Обработчик команд
import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message,ReplyKeyboardRemove
from telebot import types
TOKEN = "6555005944:AAF2jQFN2DCbwE3EjXjNzUAB5TMewTIB_YU"
bot = telebot.TeleBot(TOKEN)

with open("Quest.json", "r", encoding="utf-8") as f:
    quest_data = json.load(f)

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Поехали💨"))
    bot.send_message(message.chat.id, f"💫Привет, {message.from_user.first_name}, меня зовут {bot.get_my_name().name}.💫"
                                      f"\n⚡️Ты попал в бот-квест!⚡️"
                                      f"\nЧтобы начать нажмите на кнопку \"Поехали💨\""
                                      f"\n❗️Чтобы подробнее ознакомиться с ботом, напиши /help.❗️", reply_markup=markup)
    with open("media/start_picture.jpg", "rb") as f:
        bot.send_photo(message.chat.id, f)




@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.chat.id, f"🌞Доброго врмени суток🌚"
                                      f"\n💫Сегодня ты можешь пройти невероятно интересный квест, созданный по мотивам фильма \"Побег из шоушенка\", но с небольшими доработками💫."
                                      f"\n💥Суть заключается в том, что ты должен совершать верные решения от которых зависит твоя жизнь💥."
                                      f"\n🚨Малейший неверный ход и тебя опять закинут за решетку🚨. "
                                      f"\n🤫Будь осторожен и внимателен🤫"
                                      f"\nЕсли готов к прохождению жми \"Поехали💨\"")



@bot.message_handler(content_types=["text"])
def handle_questions_1_1_location(message: Message):
    if message.text == "Поехали💨":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_captions = quest_data["location1_1"]["buttons"]
        for s in button_captions:
            button = types.KeyboardButton(s)
            markup.add(button)

        with open(quest_data["location1_1"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)

        bot.send_message(message.chat.id, quest_data["location1_1"]["description"], reply_markup=markup)

    #location 2.1 (Вариант 1)
    elif message.text == "Бежать как можно быстрее.":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_captions = quest_data["location2_1"]["buttons"]
        for s in button_captions:
            button = types.KeyboardButton(s)
            markup.add(button)
        bot.send_message(message.chat.id, quest_data["location2_1"]["description"], reply_markup=markup)


        with open(quest_data["location2_1"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)

    #location 3.1 вариант 1 Проигрышный
    elif message.text == "Украсть ключи и одежду":
        with open(quest_data["location3_1"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
        bot.send_message(message.chat.id, quest_data["location3_1"]["description"])
        bot.send_message(message.chat.id, quest_data["location3_1"]["lose_text"], reply_markup=ReplyKeyboardRemove())

    #location 3.2 вариант 2 Проигрышный
    elif message.text == "Спрататься во время прогулки":
        with open(quest_data["location3_2"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
        bot.send_message(message.chat.id, quest_data["location3_2"]["description"])
        bot.send_message(message.chat.id, quest_data["location3_2"]["lose_text"], reply_markup=ReplyKeyboardRemove())

    #location 2.2 Вариант 2
    elif message.text == "Сбежать через время, продумав план.":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        button_captions = quest_data["location2_2"]["buttons"]
        for s in button_captions:
            button = types.KeyboardButton(s)
            markup.add(button)
        with open(quest_data["location2_2"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
        bot.send_message(message.chat.id, quest_data["location2_2"]["description"], reply_markup=markup)

    elif message.text == "Познакомиться с Рэдом":
        with open(quest_data["location3_3"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
            bot.send_message(message.chat.id, quest_data["location3_3"]["description"])
        bot.send_message(message.chat.id, quest_data["location3_3"]["win_text"], reply_markup=ReplyKeyboardRemove())

    elif message.text == "Познакомиться с Бруксом":
        with open(quest_data["location3_4"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
        bot.send_message(message.chat.id, quest_data["location3_4"]["description"])
        bot.send_message(message.chat.id, quest_data["location3_4"]["lose_text"], reply_markup=ReplyKeyboardRemove())

    elif message.text == "Остаться в тюрьме отбывать два пожизненных заключения.":
        with open(quest_data["location2_3"]["picture_file_name"], "rb") as f:
            bot.send_photo(message.chat.id, f)
        bot.send_message(message.chat.id, quest_data["location2_3"]["description"])
        bot.send_message(message.chat.id, quest_data["location3_4"]["lose_text"], reply_markup=ReplyKeyboardRemove())
















bot.polling()