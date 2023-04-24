# programa que aumneta o salario com if e else

salario = float(input('Digite o seu salario: '))
if salario > 1.250:
    aumento = (salario * 10 / 100) + salario
    print('Seu novo salario será de : {:.2f}'.format(aumento))
else:
    aumento = (salario * 15 / 100) + salario
    print('Seu salario será de: {:.2f}'.format(aumento))