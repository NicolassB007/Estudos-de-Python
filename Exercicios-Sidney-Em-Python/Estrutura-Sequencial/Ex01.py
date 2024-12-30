n = input("Informe o primeiro valor: ")
n2 = input("Informe o segundo valor: ")
n3 = input("Informe o terceiro valor: ")

n_convertido = 0
n2_convertido = 0
n3_convertido = 0
valores_validos = None

try:
    n_convertido = int(n)
    n2_convertido = int(n2)
    n3_convertido = int(n3)
    valores_validos = True
except:
    valores_validos = None

if valores_validos is True:
    resultado = (n_convertido + n2_convertido) * n3_convertido
    print(f"O RESULTADO DA SOMA DE {n} + {n2} x {n3} é {resultado}")
else:
    print("Um dos valores são inválidos")