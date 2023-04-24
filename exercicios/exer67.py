# programa que le um n umero e mostra a sua tabuada, se numero for negativo oi programa para: 

num = 0
c = 1
while True:
    num = int(input('Digite um numero para ver a sua tabuada: '))
    if num < 0:
        break
    else:
        while c <= 10:
            print(f'{num} x {c} = {num * c}')
            c += 1
    print('='*15)
    c = 1
print('fim')