print('Contador aritmetico2')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
passo = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
fim = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:    
        print(f'{termo} - ', end='')
        cont += 1
        termo += passo
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais: '))

print(f'O total de termos exibidos foram {total}')