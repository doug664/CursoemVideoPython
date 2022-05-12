#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase com letras a')).upper().strip()
print('a frase tem {} letras A'.format(frase.count('A')))
print('A primeira lketra a aparece na posicão {}'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))

