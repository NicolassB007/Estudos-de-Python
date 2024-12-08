"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para informar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Se nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
idade_convertido_int = int(idade)

if (nome and idade_convertido_int):
    nome_invertido = nome[::-1]
    tamanho_nome = len(nome)
    primeira_letra_nome = nome[0]
    ultima_letra_nome = nome[-1]
    print(f"Seu nome é {nome}")
    print(f"Você tem {idade_convertido_int} anos de idade")
    print(f"Seu nome invertido é {nome_invertido}")
    if (' ' in nome):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    print(f"Seu nome tem {tamanho_nome} letras")
    print(f"A primeira letra do seu nome é {primeira_letra_nome}")
    print(f"A ultima letra do seu nome é {ultima_letra_nome}")
else:
    print("Desculpe, você deixou campos vazios.")
