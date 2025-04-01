# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# Representados gráficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# Tipos imutáveis como valor interno

# Criando um set 
# set(iterável) ou {1, 2, 3}

# s1 = set("Luiz")
# s1 = {"Nicolas", 1, 2, 3,}
# s1 = set() # vazio
# s1 = {"Nicolas", 1, 2, 3,} # com dados
# print(s1)


# Sets são eficientes para remover valores duplicados 
# de iteráveis
# - Seus valores serão sempre únicos;
# - eles não tem indexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Nicolas')
# s1.add(3)
# s1.add(1)
# s1.update(("Olá Mundo!", 1, 2, 3))
# s1.clear()
# s1.discard(1)
# print(s1)


# Operadores úteis:
# união | união (union) - Une 
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que NÃO estão em ambos

s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5, 6}

s3 = s1 | s2 # Unindo os sets
print(s3)

s3 = s1 & s2 # Intersecção
print(s3) 

s3 = s1 - s2 # Diferença
print(s3)

s3 = s1 ^ s2 # Diferença simétrica
print(s3)