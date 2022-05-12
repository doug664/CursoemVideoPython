print('Programa que exibe pede qunto vc tem e exibe quanto em dolar vc pode comprar')

valor = float(input('Digite qunto quer gastar'))

dolar = 3.27

conversao = valor / dolar 

print('Com seus R${} reais , pode comprar US${:.3f} em dolar' .format(valor, conversao))
