"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *_ = 1, 2, 3, 4
print(x, y, _)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numeros in args:
        total += numeros
    return total

print(soma(1, 3, 4))

# Com o *args é possível ter uma quantidade indeterminada de argumentos NÃO NOMEADOS