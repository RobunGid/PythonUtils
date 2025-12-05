from random import choices, randint
from pprint import pprint
from typing import Literal, Union

SHUFFLE_LETTER_CHANCE = 0.2
SHUFFLE_SYMBOL_CHANCE = 0.1

lower_phonetic_map_ru = {
    "а": ["о"],
    "б": ["п"],
    "в": ["ф"],
    "г": ["к", "х"],
    "д": ["т"],
    "е": ["ё", "и"],
    "ё": ["е", "о"],
    "ж": ["ш", "з"],
    "з": ["с"],
    "и": ["е", "й"],
    "й": ["и"],
    "к": ["г", "х"],
    "м": ["н"],
    "н": ["м"],
    "о": ["а"],
    "п": ["б"],
    "с": ["з", "ш"],
    "т": ["д"],
    "у": ["ю"],
    "ф": ["в"],
    "х": ["г", "к"],
    "ц": ["с"],
    "ч": ["щ", "ш"],
    "ш": ["щ", "ж"],
    "щ": ["ш", "ч"],
    "ъ": ["ь"],
    "ы": ["и"],
    "ь": ["ъ"],
    "э": ["е"],
    "ю": ["у"],
    "я": ["а"]
}

lower_phonetic_map_en = {
    "a": ["e"],
    "b": ["p"],
    "c": ["k", "s"],
    "d": ["t"],
    "e": ["i", "a"],
    "f": ["v"],
    "g": ["j", "k"],
    "h": ["kh"],
    "i": ["e", "y"],
    "j": ["g"],
    "k": ["c", "g"],
    "l": ["r"],
    "m": ["n"],
    "n": ["m"],
    "o": ["u", "a"],
    "p": ["b"],
    "q": ["k"],
    "r": ["l"],
    "s": ["z"],
    "t": ["d"],
    "u": ["o"],
    "v": ["f", "w"],
    "w": ["v"],
    "x": ["ks", "z"],
    "y": ["i"],
    "z": ["s"]
}

lower_keyboard_map_en = {
    "q": ["w", "a"],
    "w": ["q", "e", "a", "s"],
    "e": ["w", "r", "s", "d"],
    "r": ["e", "t", "d", "f"],
    "t": ["r", "y", "f", "g"],
    "y": ["t", "u", "g", "h"],
    "u": ["y", "i", "h", "j"],
    "i": ["u", "o", "j", "k"],
    "o": ["i", "p", "k", "l"],
    "p": ["o", "l"],

    "a": ["q", "w", "s", "z"],
    "s": ["a", "w", "e", "d", "z", "x"],
    "d": ["s", "e", "r", "f", "x", "c"],
    "f": ["d", "r", "t", "g", "c", "v"],
    "g": ["f", "t", "y", "h", "v", "b"],
    "h": ["g", "y", "u", "j", "b", "n"],
    "j": ["h", "u", "i", "k", "n", "m"],
    "k": ["j", "i", "o", "l", "m"],
    "l": ["k", "o", "p"],

    "z": ["a", "s", "x"],
    "x": ["z", "s", "d", "c"],
    "c": ["x", "d", "f", "v"],
    "v": ["c", "f", "g", "b"],
    "b": ["v", "g", "h", "n"],
    "n": ["b", "h", "j", "m"],
    "m": ["n", "j", "k"]
}

lower_keyboard_map_ru = {
    "ё": ["й"],
    "й": ["ц", "ф"],
    "ц": ["й", "у", "ф", "ы"],
    "у": ["ц", "к", "ы", "в"],
    "к": ["у", "е", "в", "а"],
    "е": ["к", "н", "а", "п"],
    "н": ["е", "г", "п", "р"],
    "г": ["н", "ш", "р", "о"],
    "ш": ["г", "щ", "о", "л"],
    "щ": ["ш", "з", "л", "д"],
    "з": ["щ", "х", "д", "ж"],
    "х": ["з", "ъ", "ж", "э"],
    "ъ": ["х", "э"],

    "ф": ["й", "ц", "ы", "я"],
    "ы": ["ц", "у", "ф", "в", "я", "ч"],
    "в": ["у", "к", "ы", "а", "ч", "с"],
    "а": ["к", "е", "в", "п", "с", "м"],
    "п": ["е", "н", "а", "р", "м", "и"],
    "р": ["н", "г", "п", "о", "и", "т"],
    "о": ["г", "ш", "р", "л", "т", "ь"],
    "л": ["ш", "щ", "о", "д", "ь", "б"],
    "д": ["щ", "з", "л", "ж", "б", "ю"],
    "ж": ["з", "х", "д", "э"],
    "э": ["х", "ъ", "ж"],

    "я": ["ф", "ы", "ч"],
    "ч": ["ы", "в", "я", "с"],
    "с": ["в", "а", "ч", "м"],
    "м": ["а", "п", "с", "и"],
    "и": ["п", "р", "м", "т"],
    "т": ["р", "о", "и", "ь"],
    "ь": ["о", "л", "т", "б"],
    "б": ["л", "д", "ь", "ю"],
    "ю": ["д", "б"]
}
 
upper_phonetic_map_en = {letter.upper(): [x.upper() for x in lower_phonetic_map_en[letter]] for letter in lower_phonetic_map_en.keys()}
upper_keyboard_map_en = {letter.upper(): [x.upper() for x in lower_keyboard_map_en[letter]] for letter in lower_keyboard_map_en.keys()}
upper_phonetic_map_ru = {letter.upper(): [x.upper() for x in lower_phonetic_map_ru[letter]] for letter in lower_phonetic_map_ru.keys()}
upper_keyboard_map_ru = {letter.upper(): [x.upper() for x in lower_keyboard_map_ru[letter]] for letter in lower_keyboard_map_ru.keys()}

def shuffle_letters(text: str, lang: Union[Literal['ru'], Literal['en']] = 'en', mode: Union[Literal['phonetic'], Literal['keyboard']] = 'phonetic') -> str:
    lower_map = None
    upper_map = None
    match f'{lang}_{mode}':
        case 'en_phonetic':
            lower_map = lower_phonetic_map_en
            upper_map = upper_phonetic_map_en
        case 'en_keyboard':
            lower_map = lower_keyboard_map_en
            upper_map = upper_keyboard_map_en
        case 'ru_phonetic':
            lower_map = lower_phonetic_map_ru
            upper_map = upper_phonetic_map_ru
        case 'ru_keyboard':
            lower_map = lower_keyboard_map_ru
            upper_map = upper_keyboard_map_ru
        case _:
            lower_map = lower_phonetic_map_en
            upper_map = upper_phonetic_map_en
    res = ""
    for letter in text:
        index = ''.join(lower_map.keys()).find(letter.lower())
        is_upper_letter = letter.isupper()
        if index == -1:
            res += letter 
            continue
        
        new_letter = choices(upper_map[letter])[0] if is_upper_letter else choices(lower_map[letter])[0]
        if randint(1, 100) < (SHUFFLE_LETTER_CHANCE*100):
            res += new_letter
        else:
            res += letter
    return res

def shuffle_symbols(text: str) -> str:
    text_list = list(text)
    for i in range(1, len(text)-1):
        if randint(1, 100) < (SHUFFLE_SYMBOL_CHANCE*100):
            random_cofficient = choices([-1,1])[0]
            text_list[i+random_cofficient], text_list[i] = text_list[i], text_list[i+random_cofficient];
    return ''.join(text_list)


