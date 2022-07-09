# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()

for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
    
    
#jogo.sorted()



for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-='*15)
print('== RANKING DOS JOGADORES ==')


for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
    

    





#OBS para ordenar um dicionario é preciso 
# importar o itemmgetter
#colocar esse dicionario dentro de uma lista
#  combinar com o sorted() que é um metodo usado com as tuplas.
# e também com o reverse=True que faz com que fique do maior para o menor


#ex:
#sorted(jogo.items(), key=itemgetter(1))

# sendo que quando:
# key=itemgetter(0) recebe a chave do dicionario
# key=itemgetter(1) recebe o valor da chave do dicionario