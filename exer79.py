# Programa que recebe valores em uma lista e para quando o usuarios não quiser continuar e mostra a lista em ordekm crescente
lista = []

while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    if n in lista: # pode ser também 'if n not in lista:', mas ai muda a logica, entende?
        print('valor duplicado, não adicionando')
       
    else:
        print('Valor adicionando com sucesso.')
        lista.append(n)
    
    doug = str(input('Quer continuar? [S/N] ')).upper().strip()
    if doug != 'S':
        break

print(f'Você digitou os valores {lista.sort()} ')    
    