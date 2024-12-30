"""
Repetições
while
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador < 70:
    contador = contador + 1
    if contador == 4:
        print("O contador vale 4")
        continue
    if (contador >= 20) and (contador < 40):
        print("Esqueci como contar")
        continue
    print(contador)
print("Acabou")