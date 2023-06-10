salario = float(input('Informe o seu salário: R$'))
sete = 0.075 * salario
quinze = 0.15 * salario
vintedois = 0.225 * salario
vintesete = 0.275 * salario
if salario <= 1903.98:
    print('Você está isento do pagamento do imposto de renda')
else:
        if salario >= 1903.99 and salario<= 2826.65:
            print('A porcentagem a ser paga pelo imposto de renda será de 7,5%, ou seja R$', sete)
        else:
                if salario >= 2826.66 and salario<= 3751.05:
                    print('A porcentagem a ser paga pelo imposto de renda será de 15%, ou seja R$', quinze)
                else:
                    if salario >=3751.06 and salario <= 4664.68:
                        print('A porcentagem a ser paga pelo imposto de renda será de 22,5%, ou seja R$', vintedois)
                    else:
                        if salario > 4664.68:
                            print('A porcentagem a ser paga pelo imposto de renda será de 27,5%, ou seja R$', vintesete)
            
    



                