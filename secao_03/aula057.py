"""

Lista de listas e seus indeces

"""

salas = [
    ["Maria", "Helena"],
    ["Elaine"],
    ["Luiz", "João", "Eduarda"],
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][3][2])

for sala in salas:
    print("Sala: ", sala)
    for aluno in sala:
        print("Aluno: ", aluno)
    print('')
