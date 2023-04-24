# programa que lê o salario de um funciionario e calcula o novo com 15% de aumento


sal = float(input('Digite o seu salario atual'))

newsal = sal + (sal * 15 / 100)

print('Seu novo salario com aumento é de R${:.2f}'.format(newsal))