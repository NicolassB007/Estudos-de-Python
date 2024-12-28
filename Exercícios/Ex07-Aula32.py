nome = input("Informe seu nome: ")
tamanho_nome = len(nome)
if (tamanho_nome > 0) and (tamanho_nome <= 4):
    print("Seu nome é curto")
elif (tamanho_nome >= 5) and (tamanho_nome <= 6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")