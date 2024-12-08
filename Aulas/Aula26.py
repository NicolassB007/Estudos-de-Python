"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f"{variavel}")
print(f"{variavel: <10}.")
print(f"{variavel: >10}.")
print(f"{variavel: ^10}.")
print(f"{1000.67364832648:,.1f}")