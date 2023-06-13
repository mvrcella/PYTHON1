def calculate():
    print('Calculadora Simples')
    operacao = input('''
Informe a operação que você deseja fazer:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif operacao == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif operacao == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif operacao == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Operação inválida')

    again()

def again():
    novocalc = input('''
Você deseja fazer outro cálculo?
Digite S para SIM e N para NÃO
''')

    if novocalc.upper() == 'S':
        calculate()
    elif novocalc.upper() == 'N':
        print('Calculadora encerrada.')
    else:
        again()

calculate()