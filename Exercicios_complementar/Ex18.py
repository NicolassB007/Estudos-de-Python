def is_palindromo(name):
    if name == name[::-1]:
        return f"A PALAVRA {name} é uma PALINDROMO"
    return f"A PALAVRA {name} não é PALINDROMO"

any_words = input("Informe uma palavra: ").lower()
valid_name = None

letter_to_number = 0
is_number = None

try:
    for found_numbers in any_words:
        try:
            letter_to_number = int(found_numbers)
            is_number = True
        except:
            is_number = None
        if is_number is True:
            print("INSIRA UMA PALAVRA VÁLIDA!")
            break
    if is_number is None:
        valid_name = True
except:
    valid_name = None

final_name = is_palindromo(any_words)

if valid_name is True:
    print(f"{final_name}")