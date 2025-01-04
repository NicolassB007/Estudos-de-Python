"""
Iterável -> str, range, etc
Iterador -> Quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter("Nicolas")
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

texto = 'Nicolas' # iterável
# iterador = iter(texto) # iterador
# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break
for letra in texto:
    print(letra)