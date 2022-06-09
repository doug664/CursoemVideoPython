
'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

confir = 'S'
contador = soma = 0
maior = menor = 0
while confir == 'S':
    num = int(input('Digite um numero: '))
    soma += num
    contador += 1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    confir = str(input('Quer continuar [s/n]: ')).strip().upper()[0]
    

print(f'A media dos numeros é {soma/contador} \n O maior é {maior} e o Menor {menor}')
