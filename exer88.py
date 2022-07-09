from time import sleep
from random import randint

lista = []
jogos = []


print('-='*15)
print('JOGO MEGA SENA')
print('-='*15)

qtn = int(input('Quantos jogos você quer? '))

tot = 1
while tot <= qtn:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1


print(f'Sorteando {qtn} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print('fim')



