#existem 2 maneiras basicas com
# import biblioteca 
#ou
# from biblioteca import metodo

## importando a biblioteca inteira
#import math
#num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'. #format(num, math.ceil(raiz)))

## Importando um metodo/uma função da biblioteca)

from math import sqrt,floor

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('O raiz de {} é igual a {}'.format(num, floor(raiz) ))

### Para ver mais bibliotecas e metodos de bibliotecas acesse python.org - docs - escolha a versão - library reference

### usando a biblioteca random

import random
num = random.random()
#num = random.ranint(1,10) para numeros exibir nuemro aletorios com numeros interios que neste exemplo vai de 1 a 10
print(num)

