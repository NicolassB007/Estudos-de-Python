nome = 'Nicolas'
altura = 1.81
peso = 85
imc = peso / (altura ** 2)

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} metros de altura'
linha_2 = f'Pesa {peso} quilos e seu IMC é de {imc:.2f}'

print(linha_1)
print(linha_2)