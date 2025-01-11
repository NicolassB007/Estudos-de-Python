"""
Lista em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    extend - Estende a lista
    + - concatena listas
Create, Read, Update e Delete
"""

lista = [10, 20, 30, 40]
lista.append("Nicolas Bissotto")
remover_nome_da_lista = lista.pop()
print(lista, remover_nome_da_lista)

del lista[-1] # Deletando meu ultimo item
print(lista)

lista.insert(0, 5)
print(lista)
lista.clear()
print(lista)

lista.append(5)
print(lista)