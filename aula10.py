nome = str(input('Qual o seu nome'))
if nome == 'Douglas':
    print('Olá, você e legal')

print('Bomdia, {}'.format(nome))

nome2 = str(input('Qual o seu nome'))
if nome2 == 'Douglas':
    print('Olá, você e legal')
else:
    print('Seu nome não é Douglas')

print('Bomdia, {}'.format(nome))

#Programa classico

n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2 '))

media = (n1+n2)/2
print('Sua media foi {}'.format(media))
if media >= 6:
    print('Sua media foi boa')
else:
    print('Sua media foi ruim, ESTUDE MAIS')

#condição simplificada
print('PARAbéns' if media >= 6 else 'Estude mais')