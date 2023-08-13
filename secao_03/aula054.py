"""

Faça uma lista de comprar com listas
o Usuario deve ter a possibilidade de
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com
erros de indices inexistentes na lista.

"""

import os

lista_compras = []

while True:
    opcao = input("Selecione uma opção\n" 
                  "[i]nserir [a]pagar [l]istar: ").lower()

    if opcao.startswith("i"):
        os.system("cls")
        lista_compras.append(input("Produto: "))

    elif opcao.startswith("a"):
        indice_delete = input("Escolha o índice para apagar: ")

        try:
            del lista_compras[int(indice_delete)]
        except IndexError:
            print("Índice não existe na lista.")

    elif opcao.startswith("l"):
        os.system("cls")

        if len(lista_compras) == 0:
            print("Nada para listar")

        for indice, produto in enumerate(lista_compras):
            print(indice, produto)

    elif opcao == "sair":
        break
