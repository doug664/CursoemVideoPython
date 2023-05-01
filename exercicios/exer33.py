#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('numero um: '))
num2 = int(input('numero dois: '))
num3 = int(input('numero tres: '))

# verificando quem é menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2

if num3 < num1 and num3 < num2:
    menor = num3


#verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 >  num1 and num3 > num2:
    maior = num3

print(f'o menor é {menor}') # 3° forma de usar o print print(f"{variavel}")
print(f'O maior numero é o {maior}')


