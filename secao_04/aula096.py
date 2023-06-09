# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# sys.exit()  # Sai do programa
# platform = "A Minha"
# print(platform)
# print(sys.platform)
# print(platform)


# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# exit()
# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as s

# sys = "Alguma coisa"
# print(sys)
# print(s.platform)

# alias 2 - from nome_modulo import objeto as apelido
# from sys import platform as pf, exit as ex

# ex()
# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

# from sys import *

# print(platform)
# exit()
