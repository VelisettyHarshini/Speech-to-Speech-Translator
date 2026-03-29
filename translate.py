from deep_translator import GoogleTranslator

def translate_text(text, source_lang):
    translated = GoogleTranslator(source=source_lang, target='te').translate(text)

    print("Telugu:", translated)
    return translated
