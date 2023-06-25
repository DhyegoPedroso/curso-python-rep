import pprint


def pp(print):
    pprint.pprint(print, sort_dicts=False, width=60)


# lista = []

# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

# OU

lista = [(x, y) for x in range(3) for y in range(3)]


pp(lista)
