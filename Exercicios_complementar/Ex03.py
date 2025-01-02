nome_usuario = input("Digite seu nome: ").title()
valor_idade = input("Digite sua idade: ")
altura = input("Informe sua altura: ").replace(",", ".")
altura_Float = 0
altura_valida = None
try:
    altura_Float = float(altura)
    altura_valida = True
except:
    altura_valida = None

if nome_usuario.isalpha():
    print(f"Nome: {nome_usuario}")
else:
    print("APENAS LETRAS NO NOME")

if valor_idade.isdigit():
    print(f"Idade: {valor_idade}")
else:
    print("IDADE INVÁLIDA")

if altura_valida is True:
    print(f"Altura: {altura_Float}")
else:
    print("Altura INVÁLIDA")

if valor_idade.isdigit():
    maior_idade = int(valor_idade) >= 18
    if nome_usuario.isalpha():
        print(f"{nome_usuario} é MAIOR de idade? {maior_idade}")
    else:
        print(f"APENAS LETRAS NO NOME")
        print(f"MAIOR de idade? {maior_idade}")
else:
    print("IDADE INVÁLIDA")