nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome me maiusculas é: {}'.format(nome.upper()))
print('Seu nome em Minusculas é : {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))

nomediv = nome.split()
print('Seu primeio nome é {} e possui {} letras'.format( nomediv[0], len(nomediv[0])))

#Explicando
 # .upper() - deixa as letras em maiscusculas
 # .lowwer() - deixa as letras em minusculas
 # .split() - cria uma lista, onde cada nome será um elemento da lista
 # .strip() - elimina os espaços que existirem no começo e no final
 # len(alguma-coisa) - exibe a quantidade de letras e numeros
 # .count('') - exibe uma quantidade do que for passado como parametro