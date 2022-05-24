#Usando tipos primitivos
#int() - para conversões para numnero inteiro
#float() - para numeros reias
# bool() - aceita dois valores true ou false, em python a primeira letra deve ser maisculas True e False
#str() - para strings
#print('a soma vale {}',.format(s)) - usando a aprtir do python 3

#n1 = input('Digite um valor: ')
#print(type(n1))

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))

s = n1 + n2
print('A Soma de {} e {} vale {} '.format(n1,n2,s))

n = float(input('Digite um valor'))
print(n)
#print(n.isnumeric())
# usando o metodo isalgumascoisa retorna True e False, serve para testes das variaveis,
#Outros is temos
#isalpha - se é letra
# isalnum - se é alphanumerico
# isupper - se a string é toda maiuscula

#Exercicio 4 - usando  isalguma coisa

algumacoisa = input('Digite alguma coisa')

print(type(algumacoisa)) # exibe <class str>
print('Só tem espaço', algumacoisa.isspace()) #isspace retorna True ou False
print('É um numero?', algumacoisa.isnumeric())
print('É alfabetico', algumacoisa.isalpha())
print('é alfanumerico', algumacoisa.isalnum())
print('Esta em maisculas', algumacoisa.isupper())
print('Está em minusculas', algumacoisa.islower())
print('Está capitalizada', algumacoisa.istitle()) # Para strings que começam com letra maiuscula
