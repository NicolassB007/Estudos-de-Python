def convercao_celsius_fahrenheit(temperatura):
    fahrenheit = (temperatura * 1.8) + 32
    return fahrenheit

temperatura_celsius = input("Informe a temperatura em CELSIUS: ")
temperatura_celsius_float = 0.0
temperatura_celsius_valido = None

try:
    temperatura_celsius_float = float(temperatura_celsius)
    temperatura_celsius_valido = True
except:
    temperatura_celsius_valido = None

temperatura_fahrenheit = convercao_celsius_fahrenheit(temperatura_celsius_float)

if temperatura_celsius_valido is True:
    print(f"FAHRENHEIT = {temperatura_fahrenheit:.2f}")