
#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
cadastro = {}


cadastro['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['carteira'] = int(input('N° da carteira de trabalho (0 - não tem): '))

if cadastro['carteira'] != 0:
    cadastro['ano'] = int(input('Ano de Contratação'))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['ano'] + 35) - datetime.now().year)

print('-='*15)

for k, v in cadastro.items():
    print(f' - {k} tem o valor {v}')
