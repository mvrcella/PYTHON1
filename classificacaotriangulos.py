print('Informes os 3 lados do triângulo:')
a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: ')) 
if (a > b + c) or (b > a + c) or (c > a + b):
    print('Triângulo inválido')
else:
    if (a == b) and (b == c):
        print('Triângulo equilátero') 
    elif (a == b) or (b == c) or (a == c):
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')