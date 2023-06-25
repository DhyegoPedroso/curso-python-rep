# isinstace - para saber se objeto é de determinado tipo

lista = [
    "a",
    1,
    1.1,
    True,
    [
        0,
        1,
        2,
    ],
    (1, 2),
    {0, 1},
    {"nome": "Dhyego"},
]

for tipo in lista:
    if isinstance(tipo, set):
        print("SET")
        tipo.add(5)
        print(tipo, isinstance(tipo, set))
        print()

    elif isinstance(tipo, str):
        print("STR")
        print(tipo.upper())
        print()

    elif isinstance(tipo, (int, float)):
        print("NUM")
        print(tipo, tipo * 2)
        print()

    else:
        print("OUTROS")
        print(tipo)
        print()
