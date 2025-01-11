lista = ["Nicolas", "Helena", "Marcos"]
indices = 0

# Minha forma de fazer 
# for itens in lista:
#     print(f"{itens} está no indice {indices}")
#     indices += 1

# Outra forma
indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice])
