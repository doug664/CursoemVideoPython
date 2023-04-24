# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Forma 1 - importando a biblioteca

import math
num = float(input('Digite um numero'))
print('O valor digitado foi {}, e sua parte inteira é {}' .format(num, math.trunc(num)))

#Forma 2 - importando um metodo da biblioteca
from math import trunc
num = float(input('Digite um numero'))
print('O valor digitado foi {}, e sua parte inteira é {}' .format(num, trunc(num)))

#Forma 3 - Usando o metodo interno int()

num = float(input('Digite um numero'))

print('O numero é: {}\n sua parte inteira é {}' .format(num, int(num)))

