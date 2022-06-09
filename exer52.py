#descobrir sde um nuumero é primo


num = int(input('Digite o numero: '))
soma = 0
for c in range(1, num+1):
    if num % c == 0:
        soma += 1

if soma == 2:
    print(f'O numero {num} é primo')
else:
    print(f'O numero {num} não é primo')

