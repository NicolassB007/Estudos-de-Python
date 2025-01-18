"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f"{saudacao}, {nome}"
    return saudar
saudacao_1 = criar_saudacao("Bom dia", "Nicolas")
saudacao_2 = criar_saudacao("Boa noite", "Nicolas")
print(saudacao_1())
print(saudacao_2())