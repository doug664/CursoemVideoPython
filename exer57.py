# programa que ler o sexo de uma pessoa se for diferente de m ou f peça para repetir

sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0] # o zero faz o fatiamento

while sexo not in 'MmFf':
    sexo = str(input('tente novamente, Digite seu sexo[M/F]: ')).strip().upper()[0]
        
print(f'Seu sexo {sexo} foi registrado com sucesso. ')
        
    

