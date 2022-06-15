
from random import randint
contador = 0
maior = 0
menor = 0
while True:
    num = randint(1, 9)
    contador += 1

    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    print(num, end='')
    if contador == 5:
        break
print(f'\nO maior numero é: {maior}')
print(f'O menor numero é: {menor}')
print('fim')