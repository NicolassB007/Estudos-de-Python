# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como "índice"
# que vimos na lista e podem ser de tipo imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     "nome": "Nicolas"
#     "sobrenome": "Bissotto",
#     "idade": 17,
#     "altura": 1.8,
#     "endereços": [
#         {"rua": "tal, tal", "número": 123},
#         {"rua": "outra rua": "numero": 112}
#     ]
# }
pessoa = dict(nome="Nicolas", sobrenome="Bissotto")
# pessoa = {
#     "nome": "Nicolas",
#     "sobrenome": "Bissotto",
# }

pessoa = {
    "nome": "Nicolas",
    "sobrenome": "Bissotto",
    "idade": 17,
    "altura": 1.8,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}

# Acessando o dicionário
# print(pessoa, type(pessoa))
print(pessoa["endereços"])
print('\n')

for chave in pessoa:
    print(chave, pessoa[chave])