print('Conversão de segundos para horas:minutos:segundos')
print()
total_segundos = int(input('Informe número total de segundos: '))
print()
minutos = total_segundos // 60
segundos = total_segundos % 60
horas = minutos // 60
minutos %= 60
print('O resultado será igual a:')
print(horas, ':', minutos, ':', segundos)

