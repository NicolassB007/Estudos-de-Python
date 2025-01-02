valor = input("Primeiro valor: ").replace(",", ".")
valor2 = input("Segundo valor: ").replace(",", ".")

valor_float = 0
valor2_float = 0
valor_valido = None

try:
    valor_float = float(valor)
    valor2_float = float(valor2)
    valor_valido = True
except:
    valor_valido = None

if valor_valido is True:
    soma = valor_float + valor2_float
    subt = valor_float - valor2_float
    multi = valor_float * valor2_float
    divisao = valor_float / valor2_float
    print(f"SOMA = {soma:.2f}")
    print(f"SUBTRAÇÃO = {subt:.2f}")
    print(f"MULTIPLICAÇÃO = {multi:.2fDD}")
    print(f"DIVISÃO = {divisao:.2f}")
else:
    print("Um dos valores são inválidos")