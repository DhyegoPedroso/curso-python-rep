"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Fora o número a aparecer antes dos zeros
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !as 

"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:->10}')
print(f'{variavel:-<10}')
print(f'{variavel:-^10}')
print(f'{1000.4873648123746}')
print(f'{1000.4873648123746:,.1f}')
print(f'{1000.4873648123746:,.2f}')
print(f'{1000.4873648123746:+,.2f}')
print(f'{1000.4873648123746:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')