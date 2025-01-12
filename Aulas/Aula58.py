"""
Lista de listas e seus indices
"""

salas = [
    #  0         1
    ["Maria", "Helena",], # 0
    #  0
    ["Elaine",], # 1
    #    0         1         2           3 
    ["Ronaldo", "Marcos",  "Eduarda",] # 2
]

print(salas[0][1])
print(salas[2][2])
print(salas[2][1])

for sala in salas:
    for alunos in sala:
        print(alunos)