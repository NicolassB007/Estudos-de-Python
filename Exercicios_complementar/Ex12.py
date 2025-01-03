contador = 0
maior_valor = 0
menor_valor = 0
while True:
    valor = input("Valor (NATURAL): ")
    valor_int = 0
    valor_valido = None
    try:
        valor_int = int(valor)
        valor_valido = True
    except:
        valor_valido = None
    if contador == 0:
        maior_valor = valor_int
        menor_valor = valor_int
    elif (contador > 0) and (valor_int > maior_valor):
        maior_valor = valor_int
    elif (contador > 0) and (valor_int < menor_valor):
        menor_valor = valor_int
    else:
        print("ALGUM VALOR É INVÁLIDO")
        
    print(f"MAIOR VALOR {maior_valor}")
    print(f"MENOR VALOR {menor_valor}")

    sair = input("Você quer continuar(s/n)? ").lower()
    if sair.startswith('s'):
        contador += 1
        continue
    else:
        print("Você SAIU do programa!")
        break
