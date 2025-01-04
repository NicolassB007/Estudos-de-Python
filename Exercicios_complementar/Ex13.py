print(12 * "=-")
print("FIBONACCHI".center(22))
print(12 * "=-")

valor = input("Informe um valor: ")
valor_int = 0
valor_valido = None

try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None

contador = 0
valor_anterior = 0
proximo_valor = 1

if valor_valido is True:
    while contador < valor_int: 
        fibonacchi = valor_anterior + proximo_valor
        valor_anterior = proximo_valor
        proximo_valor = fibonacchi
        print(fibonacchi)
        contador += 1