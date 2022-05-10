from telebot import types
import emoji

a = ['english', 'russian', 'chinese', 'hindi', 'spanish', 'portuguese', 'french', 'italian', 'kazakh', 'ukrainian']
b = ['english_1', 'russian_1', 'chinese_1', 'hindi_1', 'spanish_1', 'portuguese_1', 'french_1', 'italian_1', 'kazakh_1',
     'ukrainian_1']
c = ['english_2', 'russian_2', 'chinese_2', 'hindi_2', 'spanish_2', 'portuguese_2', 'french_2', 'italian_2', 'kazakh_2',
     'ukrainian_2']


def keyboard_a():
    keyboard = types.InlineKeyboardMarkup()
    english = types.InlineKeyboardButton(f"English {emoji.flag_uk}", callback_data='english')
    russian = types.InlineKeyboardButton(f"Русский {emoji.flag_russia}", callback_data='russian')
    deutsch = types.InlineKeyboardButton(f"Deutsch {emoji.flag_deutsch}", callback_data='deutsch')
    chinese = types.InlineKeyboardButton(f"中国人 {emoji.flag_china}", callback_data='chinese')
    hindi = types.InlineKeyboardButton(f"हिन्दी {emoji.flag_india}", callback_data='hindi')
    spanish = types.InlineKeyboardButton(f"Español {emoji.flag_spanish}", callback_data='spanish')
    portuguese = types.InlineKeyboardButton(f"Português {emoji.flag_portugal}", callback_data='portuguese')
    french = types.InlineKeyboardButton(f"Français {emoji.flag_france}", callback_data='french')
    italian = types.InlineKeyboardButton(f"Italiano {emoji.flag_italia}", callback_data='italian')
    kazakh = types.InlineKeyboardButton(f"Қазақ {emoji.flag_kazakh}", callback_data='kazakh')
    ukrainian = types.InlineKeyboardButton(f"Український {emoji.flag_ukraine}", callback_data='ukrainian')
    keyboard.add(english, russian, deutsch, chinese, hindi, spanish, portuguese, french, italian, kazakh, ukrainian)
    return keyboard


def keyboard_b():
    keyboard = types.InlineKeyboardMarkup()
    english = types.InlineKeyboardButton(f"English {emoji.flag_uk}", callback_data='english_1')
    russian = types.InlineKeyboardButton(f"Русский {emoji.flag_russia}", callback_data='russian_1')
    deutsch = types.InlineKeyboardButton(f"Deutsch {emoji.flag_deutsch}", callback_data='deutsch_1')
    chinese = types.InlineKeyboardButton(f"中国人 {emoji.flag_china}", callback_data='chinese_1')
    hindi = types.InlineKeyboardButton(f"हिन्दी {emoji.flag_india}", callback_data='hindi_1')
    spanish = types.InlineKeyboardButton(f"Español {emoji.flag_spanish}", callback_data='spanish_1')
    portuguese = types.InlineKeyboardButton(f"Português {emoji.flag_portugal}", callback_data='portuguese_1')
    french = types.InlineKeyboardButton(f"Français {emoji.flag_france}", callback_data='french_1')
    italian = types.InlineKeyboardButton(f"Italiano {emoji.flag_italia}", callback_data='italian_1')
    kazakh = types.InlineKeyboardButton(f"Қазақ {emoji.flag_kazakh}", callback_data='kazakh_1')
    ukrainian = types.InlineKeyboardButton(f"Український {emoji.flag_ukraine}", callback_data='ukrainian_1')
    keyboard.add(english, russian, deutsch, chinese, hindi, spanish, portuguese, french, italian, kazakh, ukrainian)
    return keyboard


def keyboard_c():
    keyboard = types.InlineKeyboardMarkup()
    english = types.InlineKeyboardButton(f"English {emoji.flag_uk}", callback_data='english_2')
    russian = types.InlineKeyboardButton(f"Русский {emoji.flag_russia}", callback_data='russian_2')
    deutsch = types.InlineKeyboardButton(f"Deutsch {emoji.flag_deutsch}", callback_data='deutsch_2')
    chinese = types.InlineKeyboardButton(f"中国人 {emoji.flag_china}", callback_data='chinese_2')
    hindi = types.InlineKeyboardButton(f"हिन्दी {emoji.flag_india}", callback_data='hindi_2')
    spanish = types.InlineKeyboardButton(f"Español {emoji.flag_spanish}", callback_data='spanish_2')
    portuguese = types.InlineKeyboardButton(f"Português {emoji.flag_portugal}", callback_data='portuguese_2')
    french = types.InlineKeyboardButton(f"Français {emoji.flag_france}", callback_data='french_2')
    italian = types.InlineKeyboardButton(f"Italiano {emoji.flag_italia}", callback_data='italian_2')
    kazakh = types.InlineKeyboardButton(f"Қазақ {emoji.flag_kazakh}", callback_data='kazakh_2')
    ukrainian = types.InlineKeyboardButton(f"Український {emoji.flag_ukraine}", callback_data='ukrainian_2')
    keyboard.add(english, russian, deutsch, chinese, hindi, spanish, portuguese, french, italian, kazakh, ukrainian)
    return keyboard


base_lang = 'en'
input_lang = 'ru'
output_lang = 'en'

languages = {"English": 'en', "Русский": 'ru', "Deutsch": 'de',
             "中国人": 'zh-cn', "हिन्दी": 'hi', "Español": 'es',
             "Português": 'pt', "Français": 'fr',
             "Italiano": 'it', "Қазақ": 'kk', "Український": 'uk'}

instruction = "Instruction for use.\n" \
              " /choose_input_lang - choose the language you are translating from.\n" \
              " /choose_output_lang - choose the language you are translating into.\n" \
              " /help - calling this instruction."
