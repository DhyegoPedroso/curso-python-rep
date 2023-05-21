'''

Exercício
Exiba os índices da lista

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Lucia')
lista.append('Enzo')
lista.append('Dhyego')
lista.append('Patricia')
indices = range(len(lista))

for indice in indices:    
    print(indice, lista[indice], type(lista[indice]))
    indice += 1