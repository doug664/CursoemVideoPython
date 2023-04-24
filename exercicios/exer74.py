
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

# Para fezer o randint dentro de uma tupla é só repetir o randint(1, 5) cinco vezes

#Para mostrar o maior valor e o menor valor dentro da tupla é só os metodos max() e min(), que podem ser usados com tuplas
#então fica assim

num2 = (randint(1,5), randint(1,5), randint(1,5), randint(1,5), randint(1,5))
print(f'{num2}', end='')
print(f'\nmaior valor {max(num2)}, menor valor {min(num2)}')
