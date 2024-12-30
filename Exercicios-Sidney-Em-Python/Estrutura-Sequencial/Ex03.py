n = input("Informe um valor: ")

int_n = 0
numero_valido = None

try:
    int_n = int(n)
    numero_valido = True
except:
    numero_valido = None

if numero_valido is True:
    potencia = int_n ** 2
    print(f"{n} ^ 2 = {potencia}")
else:
    print("Valor inválido!")