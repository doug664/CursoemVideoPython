# programa que lê notas de alunos e exibe a media, só que as notas tem que ser adicionadas em uma lista

#Minha solução abaixo
'''alunos = []
notas = []

while True:
    notas.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    num1 = notas[1]
    notas.append(float(input('Nota 2: ')))
    num2 = notas[2]
    media = (num1 + num2)/2
    notas.append(media)
    alunos.append(notas[:])
    notas.clear()
    doug = str(input('Quer continuar: ')).upper().strip()
    if doug == 'N':
        break
cont = 0
for i, c in enumerate(alunos):
        print(f' {i} - {c[0]} tem media {c[3]}')
        
while True:
    resp = int(input('Mostrar as notas de qual aluno: (999 para sair)'))
    if resp == 999:
        break
    print(f'Notas de {alunos[resp][0]} são {alunos[resp][1:3]} ')
    if resp == 999:
        break
print('fim')
'''

# Codigo de resolução do exercicio

ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/ 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*26)
    opc  = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')

