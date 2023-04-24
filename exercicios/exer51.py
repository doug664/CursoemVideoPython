termo = int(input('Primeiro termo'))
razao = int(input('Razão'))
decimo = termo + (10-1) * razao # esquema da matematica

for c in range(termo, decimo + razao, razao):
    print(f'{c}', end=' => ')
print('ACABOU!')

