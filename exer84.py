# Programa que recebe nome e pesos de pessoas e retorna quantidade, pessoas pesadas e pessoas leves

galera = []
dados = []
pesoMaior = []
pesoMenor = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        pesoMaior = pesoMenor = dados[1]
    else:
        if dados[1] > pesoMaior:
            pesoMaior = dados[1]
        if dados[1] < pesoMenor:
            pesoMenor = dados[1]
    galera.append(dados[:])
    dados.clear()
    doug = str(input('Quer continuar? [S/N] ')).upper().strip()

    if doug == 'N':
        break


print('-='*15)
print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {pesoMaior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == pesoMaior:
        print(p[0])
print(f'O menor peso foi de  {pesoMenor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == pesoMenor:
        print(p[0])
