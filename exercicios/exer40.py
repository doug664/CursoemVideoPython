
n1 = float(input('Digite a primeira nota'))

n2 = float(input('Digite a segunda nota'))

media = (n1+n2)/2

if media < 5.0:
    print(f'media do aluno: {media}\n REPROVADO')
elif media >= 5.0 or media <= 6.9:
    print(f'Media do aluno: {media}\n RECUPERAÇÃO')
else:
    print(f'Media do aluno: {media}\n APROVADO')

