# Exemplo de uso dos sets
letras_digitadas = set()
while True:
    letra = input("Digite uma letra: ")
    letras_digitadas.add(letra)
    
    print(letras_digitadas)

    if 'n' in letras_digitadas:
        print("Parabéns, você digitou a letra inicial de meu nome")
        break