# programa que ler o sexo de uma pessoa se for diferente de m ou f peça para repetir

sexo = 'F'

while sexo == 'M' or sexo == 'F':
    if sexo != 'M' or sexo != 'F':
        sexo = str(input('Digite seu sexo[M/F]: ')).upper()
    else: 
        print('Erro encontrado, você deve digitar F ou M')
        
    

