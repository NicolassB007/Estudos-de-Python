# texto = 'Python'
# tamanho_texto = len(texto)
# i = 0
# Não é a melhor forma para se fazer isso
# Pois sabemos quantas repetições serão feitas
# while i < tamanho_texto:
#     print(texto[i])
#     i += 1

# senha_salva = '123456'
# senha_digitada = ''
# repeticao = 0
# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticao}x): ')

#     repeticao += 1
# print("Aquele laço acima pode ter repetições infinitas")

texto = "Python"
# letra é uma variável definida pelo desenvolvedor
for letra in texto: # PARA (cada letra) em texto:
    print(letra)    # Exiba a letra