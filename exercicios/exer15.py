print('Programa que calcula o alguel de um carro pela quantidade de dias e kilometros')
dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos quilometros o carro rodou?'))

alguelDia = 60.00
valorKm = 0.15

totaldias = dias * alguelDia
totalkm = km * valorKm
res = totaldias + totalkm
print('Você alugou o carro por {} dias e rodou {}Km' .format(dias, km))
print('Você deve pagar: \n R${:.2f} pelo aluguel do carro \n R${:.2f} pelo total de quilometros' .format(totaldias, totalkm))
print('Total a pagar é R${:.2f}'.format(res))



