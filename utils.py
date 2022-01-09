def translator(lang, text):
    texts = {
        'en': {
            'main menu': 'Choose one of the following',
            'Tours': 'Tours',
            'Contact': 'Contact',
            'About us': 'About us',

        },
        'ru': {
            'main menu': 'Выберите одно из следующих',
            'Tours': 'Туры',
            'Contact': 'Контакт',
            'About us': 'О нас',

        }
    }

    return texts.get(lang).get(text)
