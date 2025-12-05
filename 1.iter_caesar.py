from typing import Union, Literal

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
OFFSET = ord('a')

def iter_caesar(text, mode: Union[Literal["encode"], Literal["decode"]] = "encode"):
    res = ""
    for index, letter in enumerate(text):
        if letter in ALPHABET:
            index *= -1 if mode == "decode" else 1
            letter = chr((ord(letter)+index-OFFSET)%len(ALPHABET)+OFFSET)
        res += letter
    return res
