# -*- coding: utf-8 -*-
print('Informe os dados para o cálculo dos juros')
capital = float(input('Capital: '))
taxa = float(input('Taxa de juros: '))
tempo = float(input('Tempo: '))
juros = capital * taxa * tempo / 100
print('O valor dos juros é', juros)