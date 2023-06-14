"""

Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
p1 = {
    'nome': 'Dhyego Luiz',
    'sobrenome': 'Damasco Pedroso',
    'idade': 37,
    'altura': 1.72,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

# p1 = dict(nome="Dhyego Luiz", sobrenome="Damasco Pedroso")
"""

# p1 = {
#     "nome": "Dhyego Luiz",
#     "sobrenome": "Damasco Pedroso",
#     "idade": 37,
#     "altura": 1.88,
#     "endereços": [
#         {"rua": "tal tal", "número": 123},
#         {"rua": "outra rua", "número": 321},
#     ],
# }

# print(p1["nome"])
# print(p1["sobrenome"])
# print(p1["idade"])
# print(p1["altura"])
# print("------------------------")

# # Adicionando nova chave
# p1["celular"] = "48984555789"

# # Editando o valor da chave
# p1["altura"] = 1.72

# # Deletando uma chave
# del p1["idade"]

# if p1.get("idade") is None:
#     print("ESSA CHAVE NAO EXISTE")
# else:
#     print(p1["idade"])

# print("------------------------")

# for chave in p1:
#     print(chave, p1[chave])


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    "nome": "Luiz Otávio",
    "sobrenome": "Miranda",
    "idade": 900,
}

p1.setdefault("idade", 0)
print(p1["idade"])
# print(len(p1))
# print(list(p1.keys()))
# print(list(p1.values()))
# print(list(p1.items()))

# for valor in p1.values():
#     print(valor)

# for chave, valor in p1.items():
#     print(chave, valor)

# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [["nome", "novo valor"], ["idade", 30]]
p1.update(lista)
print(p1)
