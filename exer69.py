# programa que le o sexo e a idade de pessoas e retorna valores

cont18 = 0
contMen = 0
contM20 = 0
print('CADASTRE UMA PESSOA')
print('-='*20)

while True:
        idade = int(input('Digite a idade da pessoa: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Digite o sexo: [M/F] ')).upper()[0].strip()
        if idade >= 18:
            cont18 += 1
        if sexo == 'M':
            contMen += 1
        if sexo == 'F' and idade <20:
            contM20 += 1
        
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer Continuar? [S/N]')).upper()[0].strip()
        if resp == 'N':
            break
print('-='*10)
print(f'O total de pessoas com mais de 18 anos: {cont18}')
print(f'Ao todo temos {contMen} homens cadastrados')
print(f'E temos {contM20} mulheres com menos de 20 anos')