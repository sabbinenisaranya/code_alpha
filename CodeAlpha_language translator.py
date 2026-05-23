from deep_translator import GoogleTranslator

def translate_text(text, dest_lang):
    try:
        translated = GoogleTranslator(
            source='auto',
            target=dest_lang
        ).translate(text)

        return translated

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":

    print("=== Basic Language Translator ===")
    print("Example language codes:")
    print("en=English, fr=French, hi=Hindi, te=Telugu, es=Spanish")

    text = input("Enter text to translate: ").strip()

    if not text:
        print("No text entered. Exiting.")
        exit()

    dest_lang = input("Enter target language code: ").strip().lower()

    if not dest_lang:
        print("No language code entered. Exiting.")
        exit()

    result = translate_text(text, dest_lang)

    print("\nTranslated text:")
    print(result)