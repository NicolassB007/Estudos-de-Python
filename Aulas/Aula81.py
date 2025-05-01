# List comprehension em Python
# List comprehension é uma forma rápida de criar listas
# a partir de iteráveis

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)
# print(lista)

lista = [valor * 2 for valor in range(10)]
print(lista)