# List comprehension em Python
# List comprehension é uma forma rápida de criar listas
# a partir de iteráveis

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [valor * 2 for valor in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
# produtos = [
#     {"nome": "produto01", "preco": 20},
#     {"nome": "produto02", "preco": 10},
#     {"nome": "produto03", "preco": 30},
# ]

# novos_produtos = [
#     {**produto, "preço": produto["preco"] * 1.05} if produto["preco"] > 20 else {**produto} for produto in produtos 
# ]

# print(*novos_produtos, sep="\n")

produtos = [
    {"nome": "produto01", "preco": 20},
    {"nome": "produto02", "preco": 10},
    {"nome": "produto03", "preco": 30},
 ]

novos_produtos = [
    {**produto, "preço": produto["preco"] * 1.05} if produto["preco"] > 20 else {**produto} for produto in produtos if produto["preco"] >= 20 and produto["preco"] * 1.05 
]

# lista = list(valores for valores in range(10) if valores < 5)
print(novos_produtos, sep="\n")