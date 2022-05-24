#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

nome = str(input('Qual o seu nome'))
if nome == 'Douglas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem popular no brasil')

elif nome in 'Ana Claudia Jéssica Juliana':
    print('Seu nome é feminino')
else:
    print('Seu nome é tão normal')

print(f'Olá seja bem vindo {nome}')