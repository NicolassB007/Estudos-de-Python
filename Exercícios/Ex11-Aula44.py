# Em andamento
print(10 * "---")
print("PALAVRA SECRETA".center(30))
print(10 * "---")

palavra_secreta = 'Maçã'.casefold()
tamanho_palavra_secreta = len(palavra_secreta)

letra = ''
print("PALAVRA SECRETA -> ", tamanho_palavra_secreta * '*')
tentativas = 0

while True:
    palavra_usuario = input("Informe uma letra: ").casefold()
    tamanho_palavra_usuario = len(palavra_usuario)

    # Checando se a letra informada foi APENAS uma
    if tamanho_palavra_usuario > 1:
        print("APENAS UMA LETRA!")
        print("\n")
        continue

    # Checando se a letra informada realmente é uma LETRA
    if palavra_usuario.isalpha():
        letra = palavra_usuario
    else:
        print("LETRA INVÁLIDA")
        print("\n")
        continue
    
    indice_palavra = 0
    letra_correta = ''
    while indice_palavra < tamanho_palavra_secreta:
        if letra == palavra_secreta[indice_palavra]:
            letra_correta = letra
        indice_palavra += 1
    
    if tentativas == 0:
        nova_palavra = ''
    else:
        palavra_final = nova_palavra
        nova_palavra = ''
    contador = 0
    while contador < tamanho_palavra_secreta:
        if letra_correta == palavra_secreta[contador]:
            nova_palavra += letra_correta
        else:
            nova_palavra += '*'
        contador += 1
    tentativas += 1