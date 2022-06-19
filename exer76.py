#exibindo uma listagem de produtos , que estão dentro de uma tupla

lista = ('Lapis', 2, 'Caderno', 15.00, 'Mochila', 60.00, 'Estojo', 5, 'Livro', 30.00 )

print('-'*20)
print(f'{"Lista de produtos":^20}')
print('-'*20)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<5}  ', end='---')
    else:
        print(f' R$ {lista[pos]}')