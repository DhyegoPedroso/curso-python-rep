# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  D H Y E G O
# -6-5-4-3-2-1

'''

nome = 'Dhyego'

print(nome[2])
print(nome[-4])
print('----in----')
print('Dhy' in nome)
print('z' in nome)
print('----not in----')
print('Dhy' not in nome)
print('z' not in nome)

'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em nome {nome}')
else:
    print(f'{encontrar} não está em {nome}')