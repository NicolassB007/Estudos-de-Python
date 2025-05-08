# Módulos padrão do Python (import, from, as, *)
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagem: nomes grandes
# import sys
# sys.exit()


# partes - from nome_modulo as apelido
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform
# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s
# print(s.path)

# alias 2 - from nome_modulo import objeto as apelido 
# Vantagens: você pode reservar nomes para o seu código
# Desvantagens: pode ficar fora do padrão da linguagem
from sys import exit as ex
from sys import platform as pf

print(pf)

# *má prática* - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo