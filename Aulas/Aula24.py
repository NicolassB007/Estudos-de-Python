# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('á' in nome)
# print('á' in nome)
# print('á' in nome)
# print('Zo' not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que quer encontrar: ");

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"Encontrar não está em {nome}")
