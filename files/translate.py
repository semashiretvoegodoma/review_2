from googletrans import Translator


def translate(text_message, input_lang, output_lang):
    translator = Translator()
    result = translator.translate(text_message, src=input_lang, dest=output_lang)
    return result.text

# если у меня получится получить Translate API от Яндекса, то разумеется сделаю с парсингом. Я знаю как. Единственная сложность - получить этот API.
