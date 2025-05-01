# Empacotamento e Desempacotamento de Dicionários

a, b = 1, 2
a, b = b, a
# print(a, b) 

# a, b = pessoa.values()
# a, b = pessoa.items()
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)



pessoa = {
    "nome": "Nicolas",
    "sobrenome": "Bissotto",
}


dados_pessoa = {
    "idade": 16,
    "altura": 1.85
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e kwargs
# kwargs - Keyword arguments (Argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(*args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome="Nicolas", sobrenome="Bissotto", idade=17)

tupla = (1, 5, 1, "Olá")

mostro_argumentos_nomeados(**pessoa_completa)
print("\n")
# print("NAO NOMEADOS: ", end="")
# mostro_argumentos_nomeados(*tupla)