# def par_or_impar(numero):
#     if numero % 2 == 0:
#         print("PAR!")
#     else:
#         print("ÍMPAR!")

def par_or_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é PAR"
    return f"{numero} é ÍMPAR"


valor = input("Informe um valor: ")
valor_valido = None
valor_int = 0

try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None
    print("Informe um valor válido!")


# print(f"O VALOR {par_or_impar(valor_int)}")

# print(par_or_impar(valor_int))