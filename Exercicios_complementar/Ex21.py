def arithmetic_average(numbers):
    accountant = 1
    sum_result = sum(numbers)
    for qtd_itens in numbers:
        accountant += 1
    average_result = sum_result / accountant
    return average_result

list_numbers = []
quantity_numbers = input("Quantos valores serão? ")

valid_number = None
int_qtd_number = 0

try:
    int_qtd_number = int(quantity_numbers)
    valid_number = True
except:
    valid_number = None

int_number_reported = 0

if valid_number is True:
    for item in range(int_qtd_number):
        numbers_reported = input("Valor: ")
        try:
            int_number_reported = int(numbers_reported)
            valid_number = True
        except:
            valid_number = None
        if valid_number is True:
            list_numbers.append(int_number_reported)

final_average = arithmetic_average(list_numbers)
print(f"A MÉDIA ARITMÉTICA É {final_average:.2f}")