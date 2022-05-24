#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casaValor = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario'))

anos = int(input('Quantos anos voce vai pagar?'))
qtdMeses = anos * 12
parcelas = casaValor / qtdMeses
basecalculo = salario * 30 / 100

if basecalculo < parcelas:
    print(f'Infelismente seu emprestimo está negado, você não possui renda para pagar no tempo de {anos} anos')
else:
    print(f'valor casa: {casaValor:.2f}\n Total de parcelas em {anos} anos: {qtdMeses} parcelas\n Valor das parcelas: {parcelas:.2f}')
