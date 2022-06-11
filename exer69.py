# programa que le o sexo e a idade de pessoas e retorna valores

cont18 = 0
contMen = 0
contM20 = 0
print('CADASTRE UMA PESSOA')
print('-='*20)
segue = 'S'
while True:
    if segue == 'S':
        idade = int(input('Digite a idade da pessoa: '))
        sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()
        if sexo >= 18:
            cont18 += 1
        if sexo == 'M':
            contMen += 1
        if sexo == 'F' and idade <20:
            contM20 += 1
        segue = str(input('Quer Continuar? [S/n]')).upper().strip()
    else:
        break

