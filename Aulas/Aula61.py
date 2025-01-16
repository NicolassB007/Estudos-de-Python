"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f"{x=} {y=} {z=}", '|', "x + y + z = ", x + y + z)

# Executando a função
soma(2, 4)

# Usando argumentos nomeados
soma(x=2, y=4)

# Não é possível ter um argumento nomeado no meio
# Ex.:
soma(2, y=3, 6) # INVÁLIDO!

# Todos os argumentos que vem depois de um argumento nomeado tem que 
# ser nomeado
soma(2, y=3, z=6) # VÁLIDO