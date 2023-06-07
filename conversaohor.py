print('Conversão de H:M:S para Segundos')
print()
print('Informe os dados')
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
total_segundos = horas * 60 * 60 + minutos * 60 + segundos
print('O total de segundos é:', total_segundos)