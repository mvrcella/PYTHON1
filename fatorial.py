n = int(input('Informe o número para o cálculo fatorial: '))
fator = 1
for cont in range(n, 1, -1):
 fator *= cont
print('O fatorial de', n, 'é', fator)