qtd_values = int(input(("Quantos valores serão inseridos na lista: ")))
list_values = []
for values in range(qtd_values):
    values_for_list = int(input("Informe o valor: "))
    list_values.append(values_for_list)

def sum_values_in_list(list):
    # addition = 0
    # for values in list:
    #     addition += values
    return sum(list)


result = sum_values_in_list(list_values)
max_value_list = max(list_values)

print(list_values)
print(f"A soma de todos os valores da lista é {result}")
print(f"O maior valor da lista é {max_value_list}")