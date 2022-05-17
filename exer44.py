doug = "LOJAS DOUG"
print(f'{doug:=^40}')
produto = float(input('Qual o preço do produto: R$'))

op = int(input('Escolha a forma de pagamento: \n [1] - a vista\n [2] - a vista no cartao\n [3] - parcelado em 2x no cartao\n [4] - parcelado em 3x ou mais\n'))

if op == 1: 
    valorPag = produto - produto * 10 / 100
    print(f'Seu produto tem 10 por cento de desconto e o valor a pagar e: R${valorPag}')
elif op == 2:
    valorPag = produto - produto * 5 / 100
    print(f'Seu produto tem 5 poir cento de desconto e o valor a pagar e: R${valorPag}')
elif op == 3:
    valorPag = produto / 2
    print(f'Seu produto deve ser pago em 2 parcelas de: R$  {valorPag} ')
elif op == 4:
    parcelas = int(input('Em quantas vezes voce quer parcelar: '))
    prodJuros = produto + produto * 20 /100
    valorPag = prodJuros / parcelas
    print(f'Seu produto deve ser pago em {parcelas} parcelas de R$ {valorPag} ')
else:
    print('Opção invalida, tente novamente!')
    
    