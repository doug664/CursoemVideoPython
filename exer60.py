print('Contador aritmetico1')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
passo = int(input('Qual é o passo: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo} - ', end='')
    cont += 1
    termo += passo

print('FIM')