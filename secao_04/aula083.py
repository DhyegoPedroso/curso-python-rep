# Empacotamento e desempacotamento de dicionarios

# a, b = 1, 2
# a, b = b, a
# print(a, b)

# pessoa = {"nome": "Aline", "sobrenome": "Souza"}

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumento nomeados)

pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

dados_pessoa = {
    "idade": 37,
    "altura": 1.71,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa, dados_pessoa)
# print()
# print(pessoa_completa)
# print()


def mostro_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS: ", *args)

    for chave, valor in kwargs.items():
        print("NOMEADOS: ", chave, valor)


# mostro_argumentos_nomeados(1, 2, "Dhyego", "TELAL", nome="Joana", qlq=123)

mostro_argumentos_nomeados(**pessoa_completa)
