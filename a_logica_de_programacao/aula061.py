"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultado_digito_1s: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado_digito_1 anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado_digito_1 anterior for maior que 9:
    resultado_digito_1 é 0
contrário disso:
    resultado_digito_1 é o valor da conta

O primeiro dígito do CPF é 7
"""


cpf = "746.824.890-70"
cpf_formatado = cpf.replace(".", "")
cpf_formatado = cpf_formatado.replace("-", "")
nove_digitos = cpf_formatado[:9]
print(f"CPF informado {cpf}")

multiplicador = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    # print(int(digito_1) * multiplicador)
    resultado_digito_1 += int(digito_1) * multiplicador
    multiplicador -= 1    

# print(f'Soma de todos os Digitos é {resultado_digito_1}')
# print(f'{resultado_digito_1} Multiplicado por "10" é {resultado_digito_1*10}')
# print(f'O resto da divisao {resultado_digito_1*10} por "11" é {(resultado_digito_1*10)%11}')

primeiro_digito = (resultado_digito_1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

print("O primeiro digito do CPF é: ", primeiro_digito)
