def calculate():
    print('Calculadora Simples')
    operation = input('''
Informe a operação que você deseja fazer:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Operação inválida')

    again()

def again():
    calc_again = input('''
Você deseja fazer outro cálculo?
Digite S para SIM e N para NÃO
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Calculadora encerrada.')
    else:
        again()

calculate()