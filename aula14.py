#usando o while
# quando nãao se sabe exatamente até onde se vai use o while em vez do for
#OBS:
# quando sober o total de passos use o for
'''c = 1
while c < 10:
    print(c)
    c += 1
print('fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('fim')
'''
'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Você quer continuar [S/N] ')).upper()
print('fim')
'''

n = 1
par = 0
impar = 0
while n != 0 :
    n = int(input('Digite um valor: '))
    if n != 0 :
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Dos numeros digitados,  {par} são pares e {impar} são impares')
print('fim')





