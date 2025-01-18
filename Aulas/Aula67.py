"""
Higher Order Functions
Funções de primeira classe
"""

# Não é comum dar print dentro de funções
def saudacao(msg, nome):
    return f"{msg}! {nome}"

# Função que recebe uma função e executa a função
def executa(funcao, *args):
    return funcao(*args)

# v = saudacao("Bom dia!")

# saudacao_2 = saudacao
# v = saudacao_2("Bom dia!")
# print(v)

print(
    executa(saudacao, "Bom dia", "Clara")
)

print(
    executa(saudacao, "Boa noite", "Nicolas")
)