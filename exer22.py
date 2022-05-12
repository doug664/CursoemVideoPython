nome = str(input('digite nome: ')).strip()
print('Analizando seu nome...')
print('nome me maisculas:'+nome.upper())
print('nome me minusculas'+nome.lower())
print('nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
print('Seu primeiro ')

# outra forma seria
separa = nome.split()
print('Seu primeiro nome é {} e tem {} '.format(separa[0], len(separa[0])))
