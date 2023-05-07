#Programa que retorna um numero primo

num = int(input('Digite o numero: '))
soma = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        soma += 1
    else:
        print('\033[31m', end='')
    print(" {} ".format(c), end='')

if soma == 2:
    print(f' - O numero {num} é primo')
else:
    print(f' - O numero {num} não é primo')

