import math

def sum_tuple(*args):
    return sum(*args)

print("Informe valores")
value_quantity = input("Quantos valores serão inseridos? ")
int_quantity = 0
value_converted = None

try:      
    int_quantity = int(value_quantity)
    value_converted = True
except ValueError:
    value_converted = None

if value_converted is None:
    print("A quantidade de valores informada é inválida.")

else:
    print("Quantidade de valores informada -> ", int_quantity)
    numbers_list = []

    for values in range(int_quantity):
        value_for_list = input(f"{(values + 1)}: ")
        number_for_list_converted_to_int = None
        int_number = 0

        try:
            int_number = int(value_for_list)
            number_for_list_converted_to_int = True
        except ValueError:
            number_for_list_converted_to_int = None

        if number_for_list_converted_to_int is None:
            print("O valor inserido é inválido.")
            break
        else:
            numbers_list.append(int_number)

    print("Números na lista -> ", numbers_list)
    numbers_tuple = tuple(numbers_list)

    print("Tupla -> ", numbers_tuple)
    print("Somando os valores presente na tupla")
    print("Resultado -> ", sum_tuple(numbers_tuple))