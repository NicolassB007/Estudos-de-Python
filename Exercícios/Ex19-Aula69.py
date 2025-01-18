def multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

duplicador = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)
print(duplicador(3))
print(triplicar(3))
print(quadruplicar(3))