# programa que recebe valores em uma lista e coloca em em ordem sem usar o sort()

lista = list()

for c in range(0,5):
    n = int(input('Digite um valor para a lista: '))
    if c + n == 1:
        lista.append(n)
        print(f'Adicionando na posição 0 da lista')
    elif n > lista[-1]:
        lista.append(n)
        print(f'Adicionando no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores da lista são: {lista}')