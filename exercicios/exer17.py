# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# forma matematica

#co = float(input('Digite o cateto opsoto: '))
#ca = float(input('Digite o cateto adjacente: '))

#hip = (co ** 2 + ca ** 2) ** (1/2)

#print('A hipotenusa vale {:.2f}' .format(hip))

# Com o import da clase math

import math # pode se usar também from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hip = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}' .format(hip))