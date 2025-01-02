nome = input("Informe seu nome: ").title()
idade = input("Sua idade: ")

idade_int = 0
idade_valida = None

try:
    idade_int = int(idade)
    idade_valida = True
except:
    idade_valida = None

if nome.isalpha():
    print(f"{nome}")    
    maior_idade = idade_int >= 18
    print(f"É MAIOR DE IDADE? {maior_idade}")
else:
    print("NOME INVÁLIDO")