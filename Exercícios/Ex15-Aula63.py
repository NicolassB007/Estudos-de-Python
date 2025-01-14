import random
import os

multiplicacao = 0
soma_vezes_dez = 0
modulo_soma_vezes_dez = 0

primeiro_digito_cpf = 0
cpf_final = ''

cpf = []
resultado_multiplicacao = [] 

for numeros_para_cpf in range(9):
    numeros_cpf = random.randint(0, 9)
    cpf.append(numeros_cpf)

indice = 0
for contagem_regressiva in range(10, 1, -1):
    multiplicacao = cpf[indice] * contagem_regressiva
    resultado_multiplicacao.append(multiplicacao)
    indice += 1

soma = 0
indice = 0
for numero in resultado_multiplicacao:
    soma += numero

soma_vezes_dez = soma * 10
modulo_soma_vezes_dez = soma_vezes_dez % 11

primeiro_digito_cpf = modulo_soma_vezes_dez if modulo_soma_vezes_dez <= 9 else 0
cpf.append(primeiro_digito_cpf)

# Segunda parte - Pegar o segundo digito

multiplicacao = 0
resultado_multiplicacao = []
indice = 0

for numeros in range(11, 1, -1):
    multiplicacao = cpf[indice] * numeros
    resultado_multiplicacao.append(multiplicacao)
    indice += 1

soma = 0
indice = 0
for numero in resultado_multiplicacao:
    soma += numero

soma_vezes_dez = soma * 10
modulo_soma_vezes_dez = soma_vezes_dez % 11

segundo_digito_cpf = modulo_soma_vezes_dez if modulo_soma_vezes_dez <= 9 else 0
cpf.append(segundo_digito_cpf)

# Formatando o cpf
contador = 1
for numeros_cpf in cpf:
    cpf_final += str(numeros_cpf)
    if len(cpf_final.replace('.', '')) == 9:
        cpf_final += '-'
        contador = 0
        continue
    if contador == 3:
        cpf_final += '.'
        contador = 0
    contador += 1

print(cpf_final)