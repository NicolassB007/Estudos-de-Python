def soma_itens_lista(*args):
    total_soma_lista = 0
    for numeros in args:
        total_soma_lista += numeros
    return total_soma_lista

qtd_itens = input("Quantos valores terá na lista? ")

qtd_itens_int = 0
qtd_valido = None

try:
    qtd_itens_int = int(qtd_itens)
    qtd_valido = True
except:
    qtd_valido = None

itens_int = 0
itens_valido = None

lista_numeros = []
if qtd_valido is True:
    for qtd in range(qtd_itens_int):
        itens = input("Valor: ")
        try:
            itens_int = int(itens)
            itens_valido = True
        except:
            itens_valido = None
        
        if itens_valido is True:
            lista_numeros.append(itens_int)

resultado_soma = soma_itens_lista(*lista_numeros) 
print(f"A SOMA DE TODOS OS NÚMEROS DA LISTA É {resultado_soma}")