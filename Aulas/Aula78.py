# Função lambda em Python
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas 
# que contém apenas uma linha. Ou seja, tudo 
# deve ser contido dentro de uma única
# expressão.

# lista = [4, 2, 1, 5, 11, 91, 11,]
# # lista.sort(reverse=True)
# lista.sort(reverse=True)

lista = [
    {"nome": "Nicolas", "sobrenome": "Bissotto"},
    {"nome": "Maria", "sobrenome": "Oliveira"},
    {"nome": "Daniel", "sobrenome": "Silva"},
    {"nome": "Eduardo", "sobrenome": "Moreira"},
    {"nome": "Aline", "sobrenome": "Souza"},
]

# def ordenacao_dict(item):
#     return item['nome']


def exibir_lista(lista):
    for item in lista:
        print(item)

# lista.sort(key=lambda item: item["nome"])
lista_ordenada_por_nome = sorted(lista, key=lambda item: item["nome"])
lista_ordenada_por_sobrenome = sorted(lista, key=lambda item: item["sobrenome"])

exibir_lista(lista_ordenada_por_nome)
print("\n")
exibir_lista(lista_ordenada_por_sobrenome)