# programa que recebe o ano de nascimentode atleta e exibe qual a sua categoria

from datetime import date

anoNasc = int(input('Quasl o ano de nascimento do atleta? '))

anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print(f'Idade do atleta: {idade} anos')
    print('MIRIM')
elif idade <=14:
    print(f'Idade do atleta: {idade} anos')
    print('INFANTIL')
elif idade <=19:
    print(f'Idade do atleta: {idade} anos')
    print('JUNIOR')
elif idade <=20:
    print(f'Idade do atleta: {idade} anos')
    print('SENIOR')
else:
    print(f'Idade do atleta: {idade} anos')
    print('MASTER')