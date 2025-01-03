soma = 0
while True:
    valor = input("Valor (APENAS VALORES INTEIROS): ")
    valor_int = 0
    valor_valido = None
    try:
        valor_int = int(valor)
        valor_valido = True
    except:
        valor_valido = None
    if valor_valido is True:
        soma += valor_int
        print(f"SOMA = {soma}")
    else:
        print("VALOR INVÁLIDO!")
        print(f"VALOR ATUAL DA SOMA = {soma}")
    sair = input("Você quer continuar somando valores (s/n)? ").lower()
    if sair.startswith('n'):
        print("Você saiu!")
        print(f"O VALOR FINAL DA SOMA FOI {soma}")
        break
    else:
        continue