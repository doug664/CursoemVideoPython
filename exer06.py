num = int(input('Digite um numero'))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

print('o dobro de {} é {}'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))


# para a raiz quadrada pode-se usar a função pow() como pow (n, (1/2)) o primeiro parametro é a base, o segundo é o expoente