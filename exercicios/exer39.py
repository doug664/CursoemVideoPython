# Programa que recebe o ano de nascimento e retorna se a pessoa deve fazer o alistamento militar

from datetime import date
anoNasc = int(input('Digite seu ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - anoNasc

limite = 18

if idade < 18:
    tempo = limite - idade
    print(f'Você tem {idade} e ainda não precisa se alistar')
    print(f'faltam ainda {tempo} anos para voce se alistar')
elif idade == 18:
    print(f'Neste ano de {anoAtual} você deve fazer o alistamento')
else:
    tempo = idade - limite
    print('Se você não fez alistamento você deve fazer, pois ja passou da idade')
    print(f'Você passou {tempo} anos do alistamento')

#OBS: fazer também para exibir o ano que a pessoa que é menor ou maior de 18 vai ou deveria se alistar

