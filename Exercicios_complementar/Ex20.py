import random
import time
import os

def draw_number():
    dado = random.randint(1, 6)
    return dado

print("DADO DA SORTE!")
print("ESCREVA 's' PARA SAIR!!!!")
while True:
    print("ADIVINHE O NÚMERO DO DADO (1, 6)!!!!")
    time.sleep(1.2)
    user_choice = input("Informe o número do dado: ")

    valid_user_number = None
    int_user_number = 0

    try:
        int_user_number = int(user_choice)
        valid_user_number = True
    except:
        valid_user_number = None

    if valid_user_number is None:
        os.system("cls")
        print("INSIRA UM VALOR VÁLIDO!")
        continue

    if int_user_number < 1 or int_user_number > 6:
        os.system("cls")
        print("VOCÊ INSERIU VALORES FORA DOS VALORES PRESENTE EM UM DADO!")
        print("VALORES DO DADO: 1 ATÉ 6")
        continue

    given_number = draw_number()
    if int_user_number > 1 and int_user_number < 7 :
        if int_user_number == given_number:
            time.sleep(1.5)
            os.system("cls")
            print("PARABÉNS!! VOCÊ ACERTOU O NÚMERO SORTEADO")
            print(f"SUA ESCOLHA {int_user_number}, NÚMERO SORTEADO NO DADO {given_number}")
        else:
            time.sleep(1.5)
            os.system("cls")
            print("INFELIZMENTE VOCÊ NÃO TÊM SORTE! VOCÊ ERROU QUAL ERA O NÚMERO DO DADO")
            print(f"SEU NÚMERO ESCOLHIDO {int_user_number}")
            print(f"NÚMERO SORTEADO {given_number}")

    wanna_live = input("VOCÊ QUER CONTINUAR (s/n)? ").lower()
    if wanna_live.startswith('s'):
        os.system("cls")
        continue
    else:
        os.system("cls")
        print("OBRIGADO POR JOGAR CONOSCO!!")
        print("ESPERO QUE VOLTE NOVAMENTE PARA JOGAR CONOSCO!!")
        print("TENHA UM EXCELENTE DIA!")
        break