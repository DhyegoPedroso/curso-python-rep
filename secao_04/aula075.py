"""

Exercicios

"""

# Crie funççoes que duplicam, triplicam e quadruplicam
# o numero recebido como paramentro


def criar_funcoes(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador

    return multiplicar


duplicar_valor = criar_funcoes(2)
triplicar_valor = criar_funcoes(3)
quadruplicar_valor = criar_funcoes(4)


print("Duplicar", duplicar_valor(10))
print("Triplicar", triplicar_valor(10))
print("Quadruplicar", quadruplicar_valor(10))
