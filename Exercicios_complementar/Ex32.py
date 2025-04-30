print("Informe 5 valores para serem colocados em uma tupla")
number_list = []
conversion_success = None

try:
    for values in range(5):
        values_for_tuple = int(input(f"{(values + 1)} valor: "))
        number_list.append(values_for_tuple)
    conversion_success = True
except ValueError:
    print("O valor inserido é INVÁLIDO.")
    conversion_success = None

if conversion_success is None:
    print("Foi inserido valor inválido, não é possível prosseguir.")
else:
    numbers_tupla = tuple(number_list)

    print(f"Valores na tupla: {numbers_tupla}")
    print("Qual o valor você quer alterar? ")
    value_for_change = int(input("Valor: "))

    if value_for_change in numbers_tupla:
        value_changed = int(input("Valor novo: "))
                
        for index, number in enumerate(number_list):
            if number == value_for_change:
                number_list[index] = value_changed

        numbers_tupla = number_list
        print("Valores da tupla após a alteração:")
        print(numbers_tupla)
        
    else:
        print("O valor escolhido não está na tupla.")
        print("Não houve alteração")
        print(numbers_tupla)