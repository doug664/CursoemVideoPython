# adivinhando numero

from random import randint
from time import sleep # com esta biblioteca podemos fazer o computador esperar um determinado tempo em segundos
num = int(input('Digite um numero entre 0 e 5: '))

print('Processando . ')
sleep(1)
print('Processando .. ')
sleep(1)
print('Processando ... ')
sleep(1)
computador = randint(0,5)

if computador == num:
    print('você acertou ! o numero é {}'.format(computador))
else:
    print('Você errou o numero é {} e não {}'.format(computador, num))