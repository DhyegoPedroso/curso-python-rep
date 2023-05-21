'''

For + Range
range -> range(start, stop, step)

'''

#           Stop
numeros1 = range(10)
#           Start, Stop
numeros2 = range(5, 10)
#           Start, Stop, Step
numeros3 = range(5, 10, 2)

print('Stop')
for numero in numeros1:
    print(numero)

print('Start e Stop')
for numero in numeros2:
    print(numero)

print('Start, Stop e Step')
for numero in numeros3:
    print(numero)