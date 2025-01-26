# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    "nome": "Nicolas",
    "sobrenome": "Bissotto",
}

# nome = pessoa.pop("nome")
# print(nome)
# print(pessoa)

# ultimo_item = pessoa.popitem()
# print(ultimo_item)
# print(pessoa)

# pessoa.update({
#     "nome": "Maria",
#     "idade": 22,
# })

# pessoa.update(nome="Novo_nome", idade=20)

# tupla = (("nome", "novo_valor"), ("idade", 20))
lista = [["nome", "novo_valor"], ["idade", 20]]

pessoa.update(lista)
print(pessoa)