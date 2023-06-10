print()
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
if (n1 > n2) and (n1>n3):
    print ('O maior número é: ',n1)
else: 
   if (n2>n3):
       print ('O maior número é: ', n2)
   else:
       print('O maior número é:', n3)
      
       if (n1 == n2) and (n2 == n3):
           print('Os números informados são iguais')

