"""Calculadora com while"""
print(15 *"-")
print("CALCULADORA")
print(15 *"-")
while True:
    valor1 = input("Primeiro valor: ")
    valor2 = input("Segundo valor: ")
    operacao = input("Digite o operador (+-/*): ")

    numeros_validos = None
    valor1_convertido = 0
    valor2_convertido = 0

    try:
        valor1_convertido = float(valor1)
        valor2_convertido = float(valor2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um dos números são inválidos")
        continue

    operadores_permitidos = '+-/*'
    if operacao not in operadores_permitidos:
        print("O operador digitado é inválido")

    if len(operacao) > 1:
        print("Digite apenas um operador: ")
        continue

    print("Realizando sua conta, comfira o resultado abaixo:")
    if operacao == '+':
        print(f"{valor1} + {valor2} = {valor1_convertido + valor2_convertido}")
    elif operacao == '-':
        print(f"{valor1} - {valor2} = {valor1_convertido + valor2_convertido}") 
    elif operacao == '*':
        print(f"{valor1} * {valor2} = {valor1_convertido + valor2_convertido}")    
    elif operacao == '/':
        print(f"{valor1} / {valor2} = {valor1_convertido + valor2_convertido}")   
    else:
        print("Nunca deveria chegar aqui!")
    sair = input("Você quer sair? ").lower().startswith('s')
    if sair:
        break