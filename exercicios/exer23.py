# Ler um numero

num = int(input('Escreva um numero com 4 digitos'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o numero {}' .format(num))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))