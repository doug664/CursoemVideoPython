# programa que exibi quanto uma pessoa pode comprar em dolares


valor = float(input('Digite quanto dinheiro você tem: R$'))

# valor do dolar, 1 dolar vale 3.27
dolar = valor / 3.27

print('O valor de R${:.2f} pode comprar US${:.2f} dolares'.format(valor, dolar))

