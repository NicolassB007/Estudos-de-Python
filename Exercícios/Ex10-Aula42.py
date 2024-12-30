frase = 'O Python é uma linguagem de programação'\
        'multiparadigma' \
        'Python foi criado por Guido Van Rossun'.replace(' ', '')

i = 0
qtd_atual = 0
letra_que_mais_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]
    contador_letras = frase.count(letra_atual)

    if (qtd_atual < contador_letras):
        qtd_atual = contador_letras
        letra_que_mais_apareceu = letra_atual
    i += 1
print(f"A letra que apareceu mais vezes foi '{letra_que_mais_apareceu}', aparecendo {qtd_atual} vezes")