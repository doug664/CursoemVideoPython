# calculando se ano é bisexto
from datetime import date

ano = int(input('Que ano você quer analizar? Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year # esse codigo recebe o ano atual pelo computador, por causa do modulo datetime

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else: 
    print('O ano {} não é bissexto'.format(ano))