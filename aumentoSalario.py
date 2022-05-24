print('Aumenta em 15% o salario')
salario = float(input('Qual o valor do produto: '))

aumento = salario * 15 / 100

res = salario + aumento

print('Seu salario é {:.2f} e com o aumento fica {:.2f}' .format(salario, res))