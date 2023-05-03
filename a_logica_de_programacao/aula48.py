'''

Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista
    extend - Estende a lista
    + - concatena listas
    Create, Read, Update,  Delete
    Criar,  Ler,  Alterar, Apagar = lista[i] (CRUD)

'''

#         01234
#        -54321
# string = 'ABCDE' # 5 caracteres

# #         0    1     2                3      4
# #        -5    4     3                2      1
lista = [123, True, 'Dhyego Pedroso', 86,9, []]
print(lista[2], type(lista[2]))

lista[2] = 'Enzo Meira'
print(lista[2], type(lista[2]))

print(lista)

# Create
lista = [10, 20, 30, 40]
print(lista)
print('------------------')

# # Update
lista[2] = 300
print(lista)
print('------------------')

# # Delete
del lista[2]
print(lista)
print('------------------')

lista.append(50)
lista.pop()

lista.append(60)
lista.append(70)
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)
print('---------------')
lista_a.extend(lista_b)
print(lista_a)
print('-----------------------')

'''

Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

'''

lista_d = ['Luiz', 'Maria']
lista_e = lista_d

lista_d[0] = 'Qualquer coisa'
print(lista_d)
print(lista_e)
print('-----------------------')

lista_d = ['Luiz', 'Maria']
lista_e = lista_d.copy()

lista_d[0] = 'Qualquer coisa'
print(lista_d)
print(lista_e)


