"""

Closure e funções que retornam outras funções

"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"

    return saudar


saudacao_1 = criar_saudacao("Bom dia")
saudacao_2 = criar_saudacao("Boa noite")
print(saudacao_1("Dhyego"))
print(saudacao_2("Dhyego"))

falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

for nome in ["Dhyego", "Lucia", "Luiz"]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
