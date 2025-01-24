# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona um valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    "nome": "Nicolas",
    "sobrenome": "Bissotto",
}

# Retorna a quantidade de chaves no dicionário
print(len(pessoa))

# Retorna as chaves
print(pessoa.keys())

# Retorna os valores
print(pessoa.values())

#####################
# Retorna as chaves e valores
print(pessoa.items())

# Configura um valor padrão caso a chave não exista/encontrada
print(pessoa.setdefault("idade", "Chave não encontrada"))