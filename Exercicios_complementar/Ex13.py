print(10 * "=-")
print("FIBONACCHI".center(18))
print(10 * "=-")
# Em andamento

valor = input("Informe um valor: ")
valor_int = 0
valor_valido = None
try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None

contador = 0
proximo_valor = 1
while contador < valor_int:
    valor_anterior = ...
    fibonacchi = valor_anterior + proximo_valor
    proximo_valor = fibonacchi
    contador += 1
    print(fibonacchi)


