print(10* "=-") 
print("TABUADA".center(20))
print(10* "=-")
valor_para_tabuada = input("Digite um valor INTEIRO: ")
valor_valido = None
valor_tabuada_int = 0
try:
    valor_tabuada_int = int(valor_para_tabuada)
    valor_valido = True
except:
    valor_valido = None

contador = 0
if valor_valido is True:
    while contador <= 10:
        multiplicacao = valor_tabuada_int * contador
        print(f"{valor_para_tabuada} x {contador} = {multiplicacao}")
        contador += 1
else:
    print("O VALOR INFORMADO É INVÁLIDO!!!")