# Generator expression, Iterables e Iterators em Python

import sys

iterable = ["Eu", "Teno", "__iter__"]
iterator = iter(iterable)  # tem __iter__ e __next__

lista = [n for n in range(100)]
generator = (n for n in range(1000001))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(next(generator))
# print(next(generator))
# print(next(generator))

for numero in generator:
    print(numero)
