"""

Exercicios com funções

"""

# crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma variavel e mostra o valor da variavel


def multiplicacao(*args):
    total = 1

    for numero in args:
        total *= numero

    return total


numeros = multiplicacao(1, 2, 3, 4, 5)
print(numeros)

# crie uma função fala se um numero e par ou impar.
# retorne se o numero é par ou impar


def par_impar(x):
    if x % 2 == 0:
        return "Par"

    return "Impar"


numero = par_impar(30)
print(numero)
