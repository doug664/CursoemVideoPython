
somaidade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'------- {p} PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1

mediaIdade = somaidade / 4
print(f'A media de idade do grupo é: {mediaIdade} anos')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e seu nome é {nomeVelho}')
print(f'Ao todo temos {totmulher20} mulheres com menos de 20 anos')

