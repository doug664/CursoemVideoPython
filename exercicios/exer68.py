#Jogando par ou impar com o pc
from random import randint


print('Vamos jogar PAR ou IMpar')
print('-='*20)

soma = 0
par = ''
impar = ''
while True:
    jogador = int(input('Diga um valor: '))
    tipo = str(input( 'Par ou Impar? [P/I]')).upper()[0].strip()
    comp = randint(1, 5)
    soma = comp + jogador
    if soma % 2 == 0:
        par = 'P'
        if par == tipo:
            print(f'Você jogou {jogador} e o computador {comp}, resultado {soma} e deu Par, Você Venceu!')
        else:
            print(f'Você jogou {jogador} e o computador {comp}, resultado {soma} e deu Par, Computador Venceu!')
            print('FIM DE JOGO')
            break
    else:
        impar = 'I'
        if impar == tipo:
            print(f'Você jogou {jogador} e o computador {comp}, resultado {soma} e deu Impar, Você Venceu!')
        else:
            print(f'Você jogou {jogador} e o computador {comp}, resultado {soma}e deu Impar, Computador Venceu!')
            print('FIM DE JOGO')
            break
       
    