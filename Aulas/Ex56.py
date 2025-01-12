"""
Imprecisão do ponto flutuante
Usando o round and ceil para arredondar valores
"""
import decimal
# Biblioteca útil quando estamos trabalhando com números muito grande
# E quando precisamos de extrema precisão

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f"{numero_3:.2f}")
print(round(numero_3, 1))