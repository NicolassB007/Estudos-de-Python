# from collections import Counter

# def count_character(text):
#     return dict(Counter(text))

# print(count_character("Nicolas"))

def count_character(string):
    dict_letters_counted = {}
    for letters in string:
        if letters in dict_letters_counted:
            dict_letters_counted[letters] += 1
        else:
            dict_letters_counted[letters] = 1
    return dict_letters_counted


string = input("Informe um texto: ")
print(count_character(string))