def word(word):
    def invert_word():
        return word[::-1]
    return invert_word

inverter = word("Marcos")
print(inverter())