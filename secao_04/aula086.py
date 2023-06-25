# Dictionary Comprehension e Set Comprehension

import pprint


def pp(print):
    pprint.pprint(print, sort_dicts=False, width=40)


produto = {
    "nome": "Caneta Azul",
    "preco": 2.5,
    "categoria": "Escritório",
}


novo_dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}


# print(novo_dc)

s1 = {i for i in range(10)}
print(s1)
