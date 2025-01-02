valor = input("Digite um valor inteiro positivo: ")
valor_int = 0
valor_valido = None
try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None

contador = 0
# valor_int_maior_que_zero = valor_int > 0
if (valor_valido is True) and (valor_int > 0):
    while contador < valor_int:
        contador += 1
        print(f"Contador = {contador}")
else:
    print("VALOR INVÁLIDO")
    print("O VALOR INFORMADO OU É MENOR QUE 0 OU É VALOR REAL")