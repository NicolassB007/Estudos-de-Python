"""
Cuidado com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista = ["Nicolas", "Maria", True, 1, 3.1]
lista_b = lista.copy()


lista[0] = "Algo"
print(lista_b)
print(lista)