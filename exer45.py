# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep 
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('Suas opções: \n [0] PEDRA\n [1] PAPEL\n [2] TESOURA  ')
jogada = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print(f'O computadoe escolheu {itens[computador]}')
print(f'O jogador escolheu {itens[jogada]}')
print('-=' * 10)

if computador == 0:
   if jogada == 0:
       print('EMPATE')
   elif jogada == 1:
       print('JOGADOR VENCE')
   elif jogada == 2:
       print('COMPUTADOR VENCE')
   else:
       print('JOGADA INVALIDA')

elif computador == 1:
    if jogada == 0:
       print('COMPUTADOR VENCE')
    elif jogada == 1:
       print('EMPATE')
    elif jogada == 2:
       print('JOGADOR VENCE')
    else:
       print('JOGADA INVALIDA')

elif computador == 2:
    if jogada == 0:
       print('JOGADOR VENCE')
    elif jogada == 1:
       print('COMPUTADOR VENCE')
    elif jogada == 2:
       print('EMPATE')
    else:
       print('JOGADA INVALIDA')
else:
    print('opcao Invalida, Tente novamente')

