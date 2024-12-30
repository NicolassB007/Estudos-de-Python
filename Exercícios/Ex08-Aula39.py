nome = input("Informe seu nome: ")
tamanho_nome = len(nome)
indice_nome = 0
# while indice_nome < tamanho_nome:
#     print(f"*{nome[indice_nome]}*")
#     indice_nome += 1

# Outra forma de fazer
novo_nome = ''
while indice_nome < tamanho_nome:
    letra = nome[indice_nome]
    novo_nome += f'*{letra}'
    indice_nome += 1
print(f"{novo_nome}")