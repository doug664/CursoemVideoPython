# programa que lê varios produtos e mostrar o valor total
print('-='*20)
print('LOJA SUPER BARATÃO')
print('-='*20)
total = 0
mil = 0
vai = 'S'
while True:
    nprod = str(input('Qual o nome do produto: '))
    vprod = float(input('Qual o valor do produto: '))
    total += vprod
    if vprod > 1000:
        mil += 1
    vai = str(input('Você quer continuar? [S/N] ')).upper().strip()
    if vai != 'S':
        break