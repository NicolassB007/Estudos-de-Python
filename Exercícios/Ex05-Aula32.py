# valor = input("Informe um valor: ")

# if valor.isdigit(): # .isdigit() checa se o valor é INTEIRO
#     valor_int = int(valor)
#     checagem_par_impar = valor_int % 2 == 0

#     if checagem_par_impar:
#         print(f"O número {valor_int} é PAR")
#     else:
#         print(f"O número {valor_int} é IMPAR")
# else:
#     print("Você não digitou um número inteiro")

# Outra forma de resolver
valor = input("Informe um valor: ")

try:
    valor_int = int(valor)
    if valor_int % 2 == 0:
        print(f"O número {valor_int} é PAR")
    else:
        print(f"O número {valor_int} é IMPAR")
except:
    print("Você não digitou um número inteiro")