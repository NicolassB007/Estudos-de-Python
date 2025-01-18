import math
def area_circulo(raio):
    area = math.pi * raio
    return area

raio = input("Informe o raio: ")
raio_float = 0.0
raio_valido = None

try:
    raio_float = float(raio)
    raio_valido = True
except:
    raio_valido = None

area_do_circulo = area_circulo(raio_float)

if raio_valido is True:
    print(f"AREA DO CIRCULO = {area_do_circulo:.2f}")