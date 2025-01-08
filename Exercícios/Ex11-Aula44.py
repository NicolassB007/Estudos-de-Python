import os
palavra_secreta = 'Programação'
letras_corretas = ''
tentativas = 0
while True:
    palavra_final = ''
    letra_usuario = input("Digite uma letra: ")

    if len(letra_usuario) > 1:
        print("APENAS UMA LETRA!")
        continue

    if letra_usuario.isnumeric():
        print("Apenas letras!")
        continue

    if letra_usuario in palavra_secreta:
        letras_corretas += letra_usuario
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_corretas:
            palavra_final += letra_secreta
        else:
            palavra_final += '*'
    print(palavra_final)
    if palavra_final == palavra_secreta:
        os.system("cls")
        print("PARABÉNS! VOCÊ CONSEGUIU!")
        print(f"A PALAVRA ERA {palavra_secreta}")
        print(f"TENTATIVAS: {tentativas}x")
        break
    tentativas += 1