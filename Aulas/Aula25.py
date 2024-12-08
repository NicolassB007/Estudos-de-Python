"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Nicolas'
preco = 1000.9589
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)