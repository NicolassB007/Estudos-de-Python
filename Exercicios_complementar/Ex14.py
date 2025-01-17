def dobro(valor):
    return f"O DOBRO DE {valor} é {valor * 2}"

numero = input("Informe um valor: ")
numero_int = 0
numero_valido = None
try:
    numero_int = int(numero)
    numero_valido = True
except:
    numero_valido = None

if numero_valido is True:
    print(dobro(numero_int))