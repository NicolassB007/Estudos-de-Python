valor = input("Informe um valor: ")
i = 0

valor_valido = None
valor_convertido = 0

while i <= 10:

    try:
        valor_convertido = int(valor)
        valor_valido = True
    except:
        valor_valido = None
    if valor_valido:
        print(f"{valor_convertido} x {i} = {valor_convertido * i}")
    else:
        print("Valor inválido!!")
        valor = input("Informe um valor: ")
    i += 1