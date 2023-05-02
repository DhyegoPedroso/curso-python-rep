'''

Calculadora com while

'''

while True:

    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operacao = input('Informe a operação desejada (+ - * /): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:

        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if len(operacao) > 1:
        print('Digite apenas um operador.')
        continue

    if operacao not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if operacao == '+':
        print(
            f'O resultado da operação é {numero_1_float + numero_2_float}')
    elif operacao == '-':
        print(
            f'O resultado da operação é {numero_1_float - numero_2_float}')
    elif operacao == '*':
        print(
            f'O resultado da operação é {numero_1_float * numero_2_float}')
    elif operacao == '/':
        print(
            f'O resultado da operação é {numero_1_float / numero_2_float}')
    else:
        print('Algo de certo não está errado.')

    sair = input('Quer sair? ').lower().startswith('s')

    if sair:
        break


print('Até logo.')
