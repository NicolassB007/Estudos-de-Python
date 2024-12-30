n = input("Primeiro valor: ")
n2 = input("Segundo valor: ")

int_n = 0
int_n2 = 0
numeros_validos = None

try:
    int_n = int(n)
    int_n2 = int(n2)
    numeros_validos = True
except:
    numeros_validos = None

if numeros_validos is True:
    
    soma = int_n + int_n2
    sub = int_n - int_n2
    multi = int_n * int_n2
    divi = int_n / int_n2

    print(f"{n} + {n2} = {soma}")
    print(f"{n} - {n2} = {sub}")
    print(f"{n} + {n2} = {soma}")
    print(f"{n} / {n2} = {divi}")
else:
    print("Um dos valores são inválidos")