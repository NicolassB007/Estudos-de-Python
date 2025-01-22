# Manipulando as chaves e valores em dicionários
pessoa = {}

# Criando uma chave colocando o valor 

chave = "nome"
pessoa[chave] = "Nicolas"

pessoa["sobrenome"] = "Bissotto"

print(pessoa[chave])
print(pessoa)

pessoa[chave] = "Maria"

del pessoa["sobrenome"]
print(pessoa)
print(pessoa["nome"])

# print(pessoa.get("sobrenome"))
if pessoa.get("sobrenome") is None:
    print("NÃO EXISTE")
else:
    print(pessoa["sobrenome"])