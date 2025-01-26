# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave 
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o ultimo item adicionado
# update - Atualiza um dicionário com outro

import copy

dicionario = {
    "chave1": 1,
    "chave2": 2,
    "lista": [0, 1, 2],
}

# dicionario_2 = dicionario.copy()
# dicionario_2 = copy.copy(dicionario)
dicionario_2 = copy.deepcopy(dicionario)
dicionario_2["chave1"] = 1000
dicionario_2["lista"][1] = 21
print(dicionario)
print(dicionario_2)