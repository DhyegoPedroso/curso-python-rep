def executa(funcao, *args):
    return funcao(*args)


print(executa(lambda x, y: x + y, 2, 3))

duplica = executa(lambda m: lambda n: n * m, 5)
print(duplica(10))

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))
