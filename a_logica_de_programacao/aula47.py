'''

Faça um jogo para o usuário adivinha qual a palavra secreta.

- Você vai propor uma palavra secreta qualquer e vai dar possibilidade para
o usuário digitar apenas uma letra_digitada.

- Quando o usuário digitar uma letra_digitada, você vai conferir se a letra_digitada digitada está na palavra secreta.
    - Se a letra_digitada digitada estiver na palavra secreta; 
        exiba a letra_digitada;
    - Se a letra_digitada digitada não estiver na palavra secreta;
        exiba *.
    Faça a contagem de tentativas do seu usuário


'''

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:

    tentativas += 1

    letra_digitada = input('Digite uma letra_digitada: ')

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra_digitada.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:

        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print('Palavra Formanda:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns você ganhou')
        print(f'Você tentou: {tentativas} vezes')
        print('Fim do Jogo')
        break
