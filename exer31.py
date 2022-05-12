# program que exibe o valor da passagem para onibus

print('Viagem: 0,50 por kilomentro até 200Km\n 0,45 por kilomentro acima de 200Km')

km = float(input('Qual a distancia da sua viagem? '))

if km <= 200:
    valor = km * 0.50
    print('O valor da sua passagem é de {:.2f}'.format(valor))

else:
    valor = km * 0.45
    print('O valor da sua viagem é de {}'.format(valor))

    print('\n Fim do Programa')
