'''

Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

'''

# for letra in texto
texto = 'Dhyego' # iterável
iteratador = iter(texto) # iterator

variavel = 'While'
print()
print(f'{variavel:-^25}')
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# Ou

variavel = 'For'
print()
print(f'{variavel:-^25}')
for letra in texto:
    print(letra)
