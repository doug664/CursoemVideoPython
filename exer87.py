matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite um valor [{l}, {c}]: ')))

for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        
    
soma3 = 0
for l in range(0,3):
    soma3 += matriz[l][2]
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


