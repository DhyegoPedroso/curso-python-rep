"""

split e join com list e str
split - dividi uma string
join - une uma string

"""

# frase = "    Olha só que    , coisa interessante        "
# # lista_palavras = frase.split()
# # print(lista_palavras)

# # print('-----------------------------')
# # lista_palavras = frase.split(',')
# # print(lista_palavras)

# # print('-----------------------------')
# # for i, frase in enumerate(lista_palavras):
# #     print(lista_palavras[i].strip())


frase = "    Olha só que    , coisa interessante        "
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
    
# frases_unidas = '-'.join('abc')
frases_unidas = '-'.join(lista_frases)
print(frases_unidas)