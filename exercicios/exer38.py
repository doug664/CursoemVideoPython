num1 = int(input('escreva o numero 1: '))
num2 = int(input('escreva o numero 2: '))

if num1 > num2:
    print(f'O numero {num1} é o maior')
elif num2 > num1:
    print(f'O numero {num2} é maior')
else:
    print('Os numeros são iguais')