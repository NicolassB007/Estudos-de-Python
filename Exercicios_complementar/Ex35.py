import math
from tkinter.font import names

quantity_words = input("Quantas palavras serão inseridas: " )
int_converted = None

int_quantity = 0
float_quantity = .0

try:
    if isinstance(quantity_words, str):
        float_quantity = float(quantity_words)
        if isinstance(float_quantity, float):
            int_quantity = math.floor(float_quantity)
            int_converted = True

except ValueError:
    int_converted = None

if int_converted:
    word_list = [
        input(f"{(words + 1)}: ")
        for words
        in range(int_quantity)
    ]

    # for words in range(int_quantity):
        # word_for_list = input(f"{(words + 1)}: ")
        # word_list.append(word_for_list)

    print("Lista -> ", word_list)
    dict_word_with_quantity_words = {
        words: len(words)
        for words
        in word_list
    }

    # for words in word_list:
        # dict_word_with_quantity_words[words] = len(words)

    print(dict_word_with_quantity_words, "\n")

    print("Informando apenas nomes com 4 caracteres")
    names_with_4_characters = {
        name: len(name)
        for name
        in dict_word_with_quantity_words
        if len(name) > 4
    }

    print(names_with_4_characters)

else:
    print("Quantidade inserida é inválida")