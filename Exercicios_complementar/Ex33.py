lista_numeros = []

print("Informe 10 números")
for numeros in range(10):
    values = input(f"{(numeros + 1)}: ")
    value_converted = None
    int_value = 0
    try:
        int_value = int(values)
        value_converted = True
    except (TypeError, ValueError):
        value_converted = None
        # raise "Foi inserido um valor inválido"

    if value_converted is not None:
        lista_numeros.append(int_value)
    else:
        print("Foi inserido um valor inválido!")
        break
else:
    print("Valores na lista: ", *lista_numeros)
    print("Elevando todos os valores na lista ao quadrado")
    all_numbers_lista_square = [numeros_lista ** 2 for numeros_lista in lista_numeros]
    print("Resultado final: ", *all_numbers_lista_square)