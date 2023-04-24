#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero qualquer: '))
escolha  = int(input('Escolha a conversão: \n 1 - binario\n 2 - octal\n 3 - hexadecimal'))

if escolha == 1:
    print(f'{num} convertido para binario  é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para binario  é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para binario  é igual a {hex(num)[2:]}')
else:
    print('opcão invalida, repita novamente') 

    #OBS: ao executar vai ser exibido 
    # 0x com o numero em hexadecimal,
    # 0b com o numero em binario
    # 0o com o numero em octal
    # é assim que o python identifica numeros em suas bases

    # Para fazer com que não seja exibido na tela 0x, 0b e 0o, usamos as tecnicas de fatiamento de strings como: {hex(num)[2:]}, [2:] faz com seja exibido do 3 caractere em diante