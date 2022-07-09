#Programa que pede a nota e a media de um aluno e retorna o ststus do aluno, mas usando dicionarios

doug = {
    'nome': str(input('Nome: ')),
    'media': float(input('Média do aluno'))
}

print('-='*15)
print(f' - nome é igual a {doug["nome"]}')
print(f' - média é igual a {doug["media"]}')

if doug['media'] < 7:
    print(' -  situação do aluno é Reprovado')
else:
    print(' - situação do aluno Aprovado')

    # Solução do video dessa aula

    aluno = dict()
    aluno['nome'] = str(input('Nome: '))
    aluno['media: '] = float(input(f'Media do aluno {aluno["nome"]}: '))

    if aluno['media'] >= 7.0:
        aluno['situacao'] = 'Aprovado'
    elif aluno['media'] < 7:
        aluno['situacao'] = 'Recuperação'
    else:
        aluno['situacao'] = 'Reprovado'
    print('-='*15)

    for k, v in aluno.items():
        print(f' - {k} é igual a {v}')