print(12*"=-")
print("CALCULO FATORIAL".center(23))
print(12*"=-")
valor = input("Informe um valor inteiro: ")
valor_int = 0
valor_valido = None
try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None

contador = 1
fatorial = valor_int
while contador < valor_int:
    fatorial *= contador
    contador += 1
print(f"FATORIAL DE {valor} = {fatorial}")