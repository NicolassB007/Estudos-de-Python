def let_the_word_lower(word):
    return word.lower()

any_word = input("Informe alguma palavra: ").upper()

valid_word = None
is_number = None

letter_to_number = 0
try:
    for found_numbers in any_word:
        try:
            letter_to_number = int(found_numbers)
            is_number = True
        except:
            is_number = None
        if is_number is True:
            print("INSIRA UMA PALAVRA VÁLIDA!")
            break
    if is_number is None:
        valid_word = True
except:
    valid_word = None

final_string = let_the_word_lower(any_word)

if valid_word is True:
    print(f"{final_string}")