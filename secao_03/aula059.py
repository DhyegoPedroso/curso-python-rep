"""

Desempacotamento em chamadas
de métodos e funções

"""

string = "ABCD"
lista = ["Maria", "Helena", 1, 2, 3, "Eduarda"]
tupla = "Python", "é", "legal"
salas = [
    ["Maria", "Helena"],
    ["Elaine"],
    ["Luiz", "João", "Eduarda"],
]

# p, b, *_, ap, u = lista
# print(p, ap, u)

# for nome in lista:
#     print(nome)

# for nome in lista:
#     print(nome, end=' ')

# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep='\n')

