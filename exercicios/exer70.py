# programa que lê varios produtos e mostrar o valor total
print('-='*20)
print('LOJA SUPER BARATÃO')
print('-='*20)
total = 0
mil = 0
vai = ' '
menor = 0
contador = 0
prodBarato = ' '
while True:
    nprod = str(input('Qual o nome do produto: '))
    preco = float(input('Qual o valor do produto: R$'))
    contador += 1
    total += preco
    if preco > 1000:
        mil += 1
    if contador == 1 or preco < menor:
        menor = preco
        prodBarato = nprod
        
    vai = str(input('Você quer continuar? [S/N] ')).upper()[0].strip()
    if vai != 'S':
        break

print('{:-^10}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {mil}  produto(s) que custam mais de R$1000.00')
print(f'O produto mais barato:  {prodBarato} que custa R${menor:.2f}')