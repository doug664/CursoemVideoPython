print('Recebe o valor de um produto e retorna com descontro de 5 %')
valor = float(input('Qual o valor do produto: '))

desconto = valor * 5 / 100

res = valor - desconto

print('O produto vale R${} e com seu desconto fica no valor R${}' .format(valor, res))