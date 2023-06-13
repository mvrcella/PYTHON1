maior = float('-inf') 
menor = float('inf') 
while True:
 n = float(input('Informe um nœmero: '))
 if n > maior:
     maior = n
 if n < menor:
     menor = n
 resp = input('Deseja continuar? (S/N) ')
 if resp.lower() == 'n':
     break
print('Maior nœmero informado:', maior)
print('Menor nœmero informado:', menor)
