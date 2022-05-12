num = int(input('Digite um numero qualquer'))

dobro = num * 2
triplo = num * 3
raiz = num **(1/2)

print('O numero é {}\n seu dobro é {}\n seu triplo é {} e a raiz é {:.3f}' .format(num, dobro, triplo, raiz))

# outra forma é .format(num *2, num * 3, num**(1/2))
# usando a função pow para raiz quadrada pow(2,(1/2))