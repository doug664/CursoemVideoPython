# somando valore pares com o for

soma = 0
for i in range(0, 6+1):
 num = int(input('digite um numero interio'))
 if num % 2 == 0:
     soma += num
print(f'A soma dos valores pares: {soma}')