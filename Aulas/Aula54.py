"""
    enumerate - enumera iteráveis (índices)
"""
nomes = ["Nicolas", "Helena", "Marcos"]
nomes.append("João")

# lista_enumerada = enumerate(nomes)
# print(next(lista_enumerada))

for indices in enumerate(nomes):
    for valor in indices:
        print(valor, end=' ')
    print('\n')