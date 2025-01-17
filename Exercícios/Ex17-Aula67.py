def multiplicacao_numeros(*args):
    total_todos_numeros_multiplicados = 1
    for numeros in args:
        total_todos_numeros_multiplicados *= numeros
    return total_todos_numeros_multiplicados

# resultado = multiplicacao_numeros(2, 6, 2, 10)
# print(resultado)

qtd_valores = input("Quantos valores serão? ")

qtd_valores_valido = None
qtd_valores_para_int = 0
try:
    qtd_valores_para_int = int(qtd_valores)
    qtd_valores_valido = True
except:
    qtd_valores_valido = None
    print("Insira valores válidos!")

valores_int = 0
valores_valido = None

todos_valores = []

for numeros in range(qtd_valores_para_int):
    valores = input("Valor: ")
    try:
        valores_int = int(valores)
        valores_valido = True
    except:
        valores_valido = None
        print("Insira um valor inteiro válido!!")
    if valores_valido is True:
        todos_valores.append(valores_int)

resultado_multiplicacao = multiplicacao_numeros(*todos_valores)
print(f"RESULTADO = {resultado_multiplicacao}")