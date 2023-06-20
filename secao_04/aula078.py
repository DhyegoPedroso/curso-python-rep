# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('Dhyego')
# s1 = set()  # vazio
# s1 = {'Dhyego', 1, 2, 3}  # com dados

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s2 = {1, 2, 3, 3, 3, 3, 1}
# print(s2)

# Métodos úteis:
# add, update, clear, discard

# s3 = set()
# s3.add("Dhyego")
# s3.add(38)
# s3.add(1)
# s3.update(("Olá mundo", 1, 2, 3, 4, 5, 3, 5))
# # s3.clear #limpa o Set
# s3.discard("Olá mundo")  # Elimina um valor

# print(s3)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s4 = {1, 2, 3}
s5 = {2, 3, 4}
s6 = s4 | s5
s7 = s4 & s5
s8 = s4 - s5
s9 = s4 ^ s5

print(s6)
print(s7)
print(s8)
print(s9)
