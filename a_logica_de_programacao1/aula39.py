'''

Iterando strings com while

'''

nome = input('Digite um nome: ')
contador = 0
nome_formatado = ''

while contador < len(nome):
    nome_formatado += f'*{nome[contador]}'
    contador += 1


nome_formatado += '*'
print(nome_formatado)
print(nome_formatado.upper())
