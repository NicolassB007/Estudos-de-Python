import math

value_quantity_for_list = input("Quantos valores serão inseridos? ")
int_quantity = 0
value_converted = None
try:
    float_quantity = float(value_quantity_for_list)
    if isinstance(float_quantity, float):
        int_quantity = math.floor(float_quantity)
        value_converted = True
except ValueError:
    value_converted = None

print(f"Insira {int_quantity} números:")
number_list = []
for values in range(int_quantity):
    number = input(f"{(values + 1)}: ")

    int_number = 0
    number_converted = None

    try:
        float_number = float(number)
        if isinstance(float_number, float):
            int_number = math.floor(float_number)
            number_converted = True
    except ValueError:
        number_converted = None

    if number_converted is True:
        number_list.append(int_number)

print(f"Lista -> {number_list}")

number_list_to_set = set(number_list)

print("Set para remoção de duplicados")
print(f"Set -> {number_list_to_set}")

# list_without_duplicate_numbers = [
    # value
    # for value in number_list_to_set
# ]

list_without_duplicate_numbers = list(number_list_to_set)

print("Lista sem número repetido")
print(list_without_duplicate_numbers)