"""

args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""

# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y


def soma(*args):
    total_soma = 0

    for numero in args:
        total_soma += numero

    return total_soma


numeros = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numeros)
