import emoji as emoji
from telebot import types
import emoji

english = types.KeyboardButton(f"English {emoji.flag_uk}")
russian = types.KeyboardButton(f"Русский {emoji.flag_russia}")
deutsch = types.KeyboardButton(f"Deutsch {emoji.flag_deutsch}")
chinese = types.KeyboardButton(f"中国人 {emoji.flag_china}")
hindi = types.KeyboardButton(f"हिन्दी {emoji.flag_india}")
spanish = types.KeyboardButton(f"Español {emoji.flag_spanish}")
arabic = types.KeyboardButton(f" عربي{emoji.flag_arabic}")
portuguese = types.KeyboardButton(f"Português {emoji.flag_portugal}")
french = types.KeyboardButton(f"Français {emoji.flag_france}")
italian = types.KeyboardButton(f"Italiano {emoji.flag_italia}")
kazakh = types.KeyboardButton(f"Қазақ {emoji.flag_kazakh}")
ukrainian = types.KeyboardButton(f"Український {emoji.flag_ukraine}")

languages = {"English": 'en', "Русский": 'ru', "Deutsch": 'de',
             "中国人": 'zh-cn', "हिन्दी": 'hi', "Español": 'es',
             "عربي": 'ar', "Português": 'pt', "Français": 'fr',
             "Italiano": 'it', "Қазақ": 'kk', "Український": 'uk'}

instruction =   "Instruction for use.\n" \
                " /choose_input_lang - choose the language you are translating from.\n" \
                " /choose_output_lang - choose the language you are translating into.\n" \
                " /help - calling this instruction."

global_input_lang = ''
global_output_lang = ''
