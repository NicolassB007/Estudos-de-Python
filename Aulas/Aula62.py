"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja 
enviado para o parâmetro, o valor será 
usado.
Refatorar: editar o seu código
"""

# def soma(x, y, z=None):
#     if z is not None:
#         print(f"{x=} {y=} {z=}", '|', x + y + z)
#     else:
#         print(f"{x=} {y=} {z=}", '|', x + y + z)

# Todos os parâmetros depois de um valor padrão terão que ter um valor padrão também
def soma(x, z=None, y=None):
    if z is not None:
        print(f"{x=} {y=} {z=}", '|', x + y + z)
    else:
        print(f"{x=} {y=} {z=}", '|', x + y + z)

soma(1, 2)
soma(3, 5)
soma(100, 200)