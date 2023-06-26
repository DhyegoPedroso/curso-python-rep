# dir, hasattr e getattr em python

string = "Dhyego"
metodo = "upper"

if hasattr(string, metodo):
    print("Existe o metodo ", metodo)
    print(getattr(string, metodo)())
else:
    print("Não existe o metodo", metodo)
