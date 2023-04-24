# programa que le varios numeros coloca em uma lista e retorna dados dos numeros

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    doug = str(input('Quer continuar? [S/N]')).upper().strip()

    if doug == 'N':
        break


print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não faz da lista!')
else:
    print('O valor 5 faz parte da lista!')

