
jogador = dict()
time = list()
gols = []

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    resp = str(input('Quer Continuar? [S/N]')).upper()[0]
    
    if resp == 'N':
        break
print('-='*20)
print('cod ', end='')
# cod   jogador    gols   total
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*20)

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-'*40)


while True:
    doug = int(input('Mostrar dados de qual jogador? (999 para sair): '))
    if doug == 999:
        break
    if doug >= len(time):
        print(f'ERRO! Não existe jogador com codigo {doug}')
    else:
        print(f'== LEVANTAMENTO DE JOGADOR: {time[doug]["nome"]}')
        for i, g in enumerate(time[doug]['gols']):
            print(f' No jogo {i+1} fez {g} gols')
        print('-='*20)
print('fim')