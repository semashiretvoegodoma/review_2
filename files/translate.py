from googletrans import Translator

def translate(text_message, input_lang, output_lang):
    translator = Translator()
    result = translator.translate(text_message, src=input_lang, dest=output_lang)
    return result.text
