# programa que 3 numeros e diz qual é o maior e qaul é o menor

num1 = int(input('digite numero: '))
num2 = int(input('Digite numero: '))
num3 = int(input('Digite numero: '))

if num1 > num2:
    print(' o numero {} é o maior'.format(num1))

if num2 > num3:
    print( 'O numero {} é o menor'.format(num3))
else:
    print('O numero {} é o maior')