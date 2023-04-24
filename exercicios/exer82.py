# programa que varios numeros coloca em ula lista e retorna outras litas com o sonumeros pares e impares

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    doug = str(input('Quer continuar? [S/N] '))
    if doug in 'Nn':
        break
    for c in lista:
        if c % 2 == 0:
            pares.append(c)
        else:
            impares.append(c)
print('-='*15)
print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {pares}')
print(f'A lista de numeros impares é {impares}')