def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# funcao = lambda parametro: parametro // Não é recomendado pela PEP8

# duplica = executa(
#     lambda m: lambda n: n * m, 2
# ) // Não é muito recomendado

# print(duplica(5))

# print(
#     executa(
#         lambda x, y: x + y, 4, 5
#     )
# )