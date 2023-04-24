# Programa que exibe uma lista e mostra o maior valor e o menor valor

lista = []

for pos in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição{pos}: ')))

print('-='*10)
print(f'Os valores digitados na lista são: {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posição(s): ', end='')

for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ')

print(f'O menor valor digitado foi {min(lista)} nas posição(s): ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ')