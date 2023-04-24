print('Calculado de parade para pintura')
altura = float(input('Digite a altura da parade'))
largura = float(input('Digite a altura da parede'))

area = altura * largura

tinta = 2

res = area / tinta

print('Sua parede tem {} m² e você vai precisar de {} litros de tinta'.format(area, res))