#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoa = dict()
pessoas = list()
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] =  str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('Erro! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
   
    while True:
        doug = str(input('Quer Continuar? [S/N]')).upper()[0].strip()
        
        if doug in 'SN':
            break
        print('Erro, Responda apenas S ou N.')
    if doug == 'N':
        break



media = soma / len(pessoas)
print(f'A) Foram cadastradas {len(pessoas)} pessoas')
print(f'B) A media de idade das pessoas é {media:5.2f} anos')
print(f'As mulheres cadastradas são ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('encerrado')

