# programa que l e 2 valores e fica repetido até que a pessoa queira sair

num1 = int(input('Digite o primeiro numero: '))

num2 = int(input('Digite o segundo numero: '))

op = 0 

while op != 5 :

    op = int(input('Digite uma opção: \n[1] somar \n2] multiplicar \n[3]maior \n[4] novos numeros \n[5] sair do programa '))

    if op == 1:
        print(f'A soma de {num1} e {num2} é {num1+num2}')
    elif op == 2:
        print(f'A multiplicação de {num1} e {num2} é {num1*num2}')
    elif op == 3:
        if num1 > num2:
            print(f'O numero {num1} é maior')
        else:
            print(f'O numero {num2} é maior')

    elif op == 4:
        num1 = int(input('Digite um novo primeiro numero: '))

        num2 = int(input('Digite um novo segundo numero: '))

print('Saindo do programa - fim')