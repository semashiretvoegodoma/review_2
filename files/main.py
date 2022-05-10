from telebot import TeleBot
from telebot import types
import emoji
from translate import translate
from languages import instruction
import languages

TOKEN = '5332298321:AAHsUhdQUPwKctnQGcp2CV0YPHOoNerq_xY'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    introduction = f"{emoji.smile_hand} Hi, <b>{message.from_user.first_name} <b>{message.from_user.last_name}</b></b>\n\n" \
                   f"What language do you understand? {emoji.smile_question}\n\n" \
                   f"I need to give you instructions for use so that you understand what is written there.{emoji.smile_document}"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(languages.english, languages.russian, languages.deutsch,
               languages.chinese, languages.hindi, languages.spanish,
               languages.arabic, languages.portuguese, languages.french,
               languages.italian, languages.kazakh, languages.ukrainian)
    bot.send_message(message.chat.id, introduction, reply_markup=markup, parse_mode='html')


@bot.message_handler(content_types=['text'])
def buttons_1(message):
    global result
    get_message_bot = message.text
    keyboard = types.InlineKeyboardMarkup()

    if get_message_bot == f"Русский {emoji.flag_russia}":
        result = translate(instruction, "en", "ru")
    elif get_message_bot == f"English {emoji.flag_uk}":
        result = instruction
    elif get_message_bot[:-3] == "Deutsch":
        result = translate(instruction, "en", "de")
    elif get_message_bot[:-3] == "中国人":
        result = translate(instruction, "en", "zh-cn")
    elif get_message_bot[:-3] == "हिन्दी":
        result = translate(instruction, "en", "hi")
    elif get_message_bot[:-3] == "Español":
        result = translate(instruction, "en", "es")
    elif get_message_bot[:-3] == "عربي":
        result = translate(instruction, "en", "ar")
    elif get_message_bot[:-3] == "Português":
        result = translate(instruction, "en", "pt")
    elif get_message_bot[:-3] == "Français":
        result = translate(instruction, "en", "fr")
    elif get_message_bot[:-3] == "Italiano":
        result = translate(instruction, "en", "it")
    elif get_message_bot[:-3] == "Қазақ":
        result = translate(instruction, "en", "kk")
    elif get_message_bot[:-3] == "Український":
        result = translate(instruction, "en", "uk")
    else:
        result = "Do everything as it is written in the message above"
    bot.send_message(message.chat.id, result, reply_markup=keyboard)




# @bot.message_handler(commands=['choose_input_lang'])
# def in_lang(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     markup.add(languages.english, languages.russian, languages.deutsch,
#                languages.chinese, languages.hindi, languages.spanish,
#                languages.arabic, languages.portuguese, languages.french,
#                languages.italian, languages.kazakh, languages.ukrainian)
#     bot.send_message(message.chat.id, "Please select a language input", reply_markup=markup)
#
#     if message.text in languages.languages:
#         languages.global_input_lang = dict.get(message.text, None)
#     else:
#         bot.send_message(message.chat.id, "Do everything as it is written in the message above", reply_markup=markup)
#
#
#
# @bot.message_handler(commands=['choose_input_lang'])
# def out_lang(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     markup.add(languages.english, languages.russian, languages.deutsch,
#                languages.chinese, languages.hindi, languages.spanish,
#                languages.arabic, languages.portuguese, languages.french,
#                languages.italian, languages.kazakh, languages.ukrainian)
#     bot.send_message(message.chat.id, "Please select a language output", reply_markup=markup)
#
#
#     remove_buttons = types.ReplyKeyboardRemove()
#     if message.text in languages.languages:
#         languages.global_output_lang = dict.get(message.text, None)
#         bot.send_message(message.chat.id, "Write",
#                          reply_markup=remove_buttons)
#     else:
#         bot.send_message(message.chat.id, "Do everything as it is written in the message above", reply_markup=remove_buttons)
#
#
#
# @bot.message_handler(content_types=['text'])
# def translate(message):
#     bot.send_message(message.chat.id, translate(message, languages.global_input_lang, languages.global_output_lang))




# @bot.message_handler(commands=['help'])
# def command_help(m):
#     cid = m.chat.id
#     keyboard = types.InlineKeyboardMarkup()
#     kb1 = types.InlineKeyboardButton(text="1-ая кнопка", callback_data="text1")
#     kb2 = types.InlineKeyboardButton(text="2-ая кнопка", callback_data="text2")
#     keyboard.add(kb1, kb2)
#     msg = bot.send_message(cid, "Список:", reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda c: True)
# def ans(c):
#     cid = c.message.chat.id
#     keyboard = types.InlineKeyboardMarkup()
#     if c.data == "text1":
#         bot.send_message(cid, "Нажали 1-ю кнопку", reply_markup=keyboard)
#     elif c.data == "text2":
#         bot.send_message(cid, "Нажали 2-ю кнопку", reply_markup=keyboard)



print("Бот запущен")
bot.polling(none_stop=True)
