qtd_values = int(input("Informe quantos valores a lista terá: "))

list_values = []

for repetition in range(0, qtd_values):
    value = int(input(f"Valor {(repetition + 1)}: "))
    list_values.append(value)

print("Elevando e exibindo o resultados dos valores ao quadrado...")
list_result_square_values = []

def square(number_list):
    for values in number_list:
        list_result_square_values.append(values ** 2)

    return list_result_square_values

print("Lista com números normais.")
print(list_values)

print("Lista com o resultado dos números da lista ao quadrado.")
print(square(list_values))
