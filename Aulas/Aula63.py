"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1
def escopo():
    # O x do escopo do arquivo está sendo modificado
    global x
    x = 10

    def outra_funcao():
        # O x do escopo do arquivo está sendo modificado agora dentro do escopo
        # da função outra_funcao()
        global x
        y = 2
        x = 12
        print(x, y)

    outra_funcao()
    print(x)

print(x)
# O valor de x foi modificado
escopo()
print(x)
print(x)