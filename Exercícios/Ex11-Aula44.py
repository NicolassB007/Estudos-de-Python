import os
print(10 * "---")
print("PALAVRA SECRETA".center(30))
print(10 * "---")

palavra_secreta = 'Maçã'

letras_corretas = ''
letra = ''
tentativas = 0
palavra_final = ''

while True:
    letra_usuario = input("Informe uma letra: ")

    # Checando se a letra informada foi APENAS uma
    if len(letra_usuario) > 1:
        print("APENAS UMA LETRA!")
        print("\n")
        continue

    # Checando se a letra informada realmente é uma LETRA
    if letra_usuario.isalpha():
        letra = letra_usuario
    else:
        print("LETRA INVÁLIDA")
        print("\n")
        continue

    if letra in palavra_secreta:
        letras_corretas += letra

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print("PARABÉNS, VOCÊ ACERTOU!'")
        print(f"A palavra é {palavra_formada}")
        print(f"TENTATIVAS = {tentativas}")
        letras_corretas = ''
        tentativas = 0
    tentativas += 1