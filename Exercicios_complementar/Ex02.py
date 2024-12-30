while True:
    valor = input("Informe o primeiro valor: ")
    valor2 = input("Informe o segundo valor: ")
    operadores = input("Qual o operador (+-/*): ")

    valor_valido = None
    valor_convertido = 0
    valor2_convertido = 0

    try:
        valor_convertido = float(valor)
        valor2_convertido = float(valor2)
        valor_valido = True
    except:
        valor_valido = None

    if valor_valido is None:
        print("Um dos valores são inválidos")

    operadores_permitidos = '+-/*'
    
    if operadores not in operadores_permitidos:
        print("Operador inválido!")

    if len(operadores) > 1:
        print("Digite apenas UM operador")

    print("Realizando os calculos, veja os resultados abaixo")
    if operadores == '+':
        print(f"{valor} + {valor2} = {valor_convertido + valor2_convertido:.2f}")
    elif operadores == '-':
        print(f"{valor} - {valor2} = {valor_convertido - valor2_convertido:.2f}")
    elif operadores == '*':
        print(f"{valor} * {valor2} = {valor_convertido * valor2_convertido:.2f}")
    elif operadores == '/':
        print(f"{valor} / {valor2} = {valor_convertido / valor2_convertido:.2f}")
    elif operadores == '' or ' ':
        print("Operador inválido!")
        continue
    else:
        print("Não era para ter chegado aqui!")

    opcao_sair_programa = input("Você quer sair? ").lower().startswith('s')

    if opcao_sair_programa:
        break