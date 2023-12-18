from telebot import TeleBot
from telebot import types
import emoji
from languages import instruction
from translate import translate
import languages

TOKEN = '5332298321:AAHsUhdQUPwKctnQGcp2CV0YPHOoNerq_xY'

bot = TeleBot(TOKEN)

keyboard = types.InlineKeyboardMarkup()


@bot.message_handler(commands=['start'])
def start(message):
    introduction = f"{emoji.smile_hand} Hi, <b>{message.from_user.first_name} <b>{message.from_user.last_name}</b></b>\n\n" \
                   f"What language do you understand? {emoji.smile_question}\n\n" \
                   f"I need to give you instructions for use so that you understand what is written there.{emoji.smile_document}"
    bot.send_message(message.chat.id, introduction, reply_markup=languages.keyboard_a(), parse_mode='html')


@bot.callback_query_handler(func=lambda a: a.data in languages.a)
def translate_instruction(a):
    if a.data == "russian":
        languages.base_lang = 'ru'

    elif a.data == "english":
        languages.base_lang = 'en'

    elif a.data == "deutsch":
        languages.base_lang = 'de'

    elif a.data == "chinese":
        languages.base_lang = 'zh-cn'

    elif a.data == "hindi":
        languages.base_lang = 'hi'

    elif a.data == "spanish":
        languages.base_lang = 'es'

    elif a.data == "portuguese":
        languages.base_lang = 'pt'

    elif a.data == "french":
        languages.base_lang = 'fr'

    elif a.data == "italian":
        languages.base_lang = 'it'

    elif a.data == "kazakh":
        languages.base_lang = 'kk'

    elif a.data == "ukrainian":
        languages.base_lang = 'uk'

    bot.send_message(a.message.chat.id, translate(instruction, 'en', languages.base_lang), reply_markup=keyboard)


@bot.message_handler(commands=['choose_input_lang'])
def promeshutok_1(message):
    bot.send_message(message.chat.id, translate("Please select the language you want to translate from", 'en',
                                                languages.base_lang), reply_markup=languages.keyboard_b())


@bot.callback_query_handler(func=lambda b: b.data in languages.b)
def in_lang(b):
    if b.data == "russian_1":
        languages.input_lang = 'ru'

    elif b.data == "english_1":
        languages.input_lang = 'en'

    elif b.data == "deutsch_1":
        languages.input_lang = 'de'

    elif b.data == "chinese_1":
        languages.input_lang = 'zh-cn'

    elif b.data == "hindi_1":
        languages.input_lang = 'hi'

    elif b.data == "spanish_1":
        languages.input_lang = 'es'

    elif b.data == "portuguese_1":
        languages.input_lang = 'pt'

    elif b.data == "french_1":
        languages.input_lang = 'fr'

    elif b.data == "italian_1":
        languages.input_lang = 'it'

    elif b.data == "kazakh_1":
        languages.input_lang = 'kk'

    elif b.data == "ukrainian_1":
        languages.input_lang = 'uk'

    bot.send_message(b.message.chat.id,
                     translate("Now select another language with the command /choose_output_lang", 'en',
                               languages.base_lang),
                     reply_markup=keyboard)


@bot.message_handler(commands=['choose_output_lang'])
def promeshutok_2(message):
    bot.send_message(message.chat.id, translate("Please select the language you want to translate into", 'en',
                                                languages.base_lang), reply_markup=languages.keyboard_c())


@bot.callback_query_handler(func=lambda c: c.data in languages.c)
def out_lang(c):
    if c.data == "russian_2":
        languages.output_lang = 'ru'

    elif c.data == "english_2":
        languages.output_lang = 'en'

    elif c.data == "deutsch_2":
        languages.output_lang = 'de'

    elif c.data == "chinese_2":
        languages.output_lang = 'zh-cn'

    elif c.data == "hindi_2":
        languages.output_lang = 'hi'

    elif c.data == "spanish_2":
        languages.output_lang = 'es'

    elif c.data == "portuguese_2":
        languages.output_lang = 'pt'

    elif c.data == "french_2":
        languages.output_lang = 'fr'

    elif c.data == "italian_2":
        languages.output_lang = 'it'

    elif c.data == "kazakh_2":
        languages.output_lang = 'kk'

    elif c.data == "ukrainian_2":
        languages.output_lang = 'uk'

    bot.send_message(c.message.chat.id, translate("Super. Write", 'en', languages.base_lang), reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, translate(instruction, 'en', languages.base_lang))


@bot.message_handler(content_types=['text'])
def perevodchik(message):
    bot.send_message(message.chat.id, translate(message.text, languages.input_lang, languages.output_lang))


print("Бот запущен")
bot.polling(none_stop=True)
