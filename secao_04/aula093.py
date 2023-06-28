# Try, except, else e finally

a = 18
b = 0
# b = 2
# c = a / b

try:
    c = a / b
    # print(b[0])
    print("Linha 1 "[1000])

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print("Alguma variavel nao foi definida")
except (TypeError, IndexError) as error:
    print("Objeto não é subscritível")
    print("MSG: ", error)
    print("Nome: ", error.__class__.__name__)
except Exception:
    print("ERRO DESCONHECIDO")


print("CONTINUAR")
