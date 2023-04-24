from random import randint

print('Pensei em um numero entre 0 e 10, tente adivinhar!!!')

comp = randint(0, 10)

jogador = int(input('Digite seu numero: '))
tentativas = 0
while comp != jogador:
    jogador = int(input('Digite outro numero: '))
    tentativas += 1

print(f'Você acertou, e tentou {tentativas} vezes')

'''
variando para dicas com if e else

if jogador < computador:
    print( mais, digitou novamente)
else:
    print(menos , digite outro numero)
'''