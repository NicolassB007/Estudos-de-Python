# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados gráficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# Tipos imutáveis como valor interno

# Criando um set 
# set(iterável) ou {1, 2, 3}

# s1 = set("Luiz")
# s1 = {"Nicolas", 1, 2, 3,}
s1 = set() # vazio
s1 = {"Nicolas", 1, 2, 3,} # com dados
print(s1)


# Sets são eficientes para remover valores duplicados 
# de iteráveis
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard