maior = float('-inf') 
menor = float('inf') 
while True:
 n = float(input('Informe um n�mero: '))
 if n > maior:
     maior = n
 if n < menor:
     menor = n
 resp = input('Deseja continuar? (S/N) ')
 if resp.lower() == 'n':
     break
print('Maior n�mero informado:', maior)
print('Menor n�mero informado:', menor)
