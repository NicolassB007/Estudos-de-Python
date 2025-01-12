"""
split e join com list e str
split - Divide uma string (Retorna uma lista)
join - une uma string
"""

frase = "Olha só que, coisa interessante"
lista_palavra = frase.split()
lista_frase = frase.split(',')
print(lista_frase)

frase_unidas = ' '.join(lista_palavra)
print(frase_unidas)