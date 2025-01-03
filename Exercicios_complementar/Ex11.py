valor = input("Informe um valor (NATURAL): ")
valor_int = 0
valor_valido = None
try:
    valor_int = int(valor)
    valor_valido = True
except:
    valor_valido = None
contador = 2
contador_divisao_sem_resto = 0
if valor_valido is True:
    while contador <= valor_int:
        if valor_int % contador == 0:
            contador_divisao_sem_resto += 1
        contador += 1
    if contador_divisao_sem_resto > 1:
        print(f"O VALOR {valor} NÃO é PRIMO")
    else:
        print(f"O VALOR {valor} É PRIMO")