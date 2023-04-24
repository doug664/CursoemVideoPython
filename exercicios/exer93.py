
jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
soma = 0
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))

jogador['gols'] = gols

for c in gols:
    soma += c 
    #OBS pode ser usado  o sum(gols)

jogador['total'] = soma
print('-='*19)

print(jogador)
print('-='*19)


for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*19)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for c in range(0, len(jogador['gols'])):
    print(f'==> Na partida {c+1}, fez {jogador["gols"][c]} gols')


#Obs: Para somar valores numeros dentro de uma lista de forma facil com o recurso do python use:
#sum(gols) retorna o total numero dos valores dentro da lista

# OUtra forma para usar o for para exibir as partidas e o totalk de gol por partida é 
'''
for i, v in enumarate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols')

'''