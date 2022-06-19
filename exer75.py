num1 = int(input('Digite um numero: '))

if num1 >= 0:
    num2 = int(input('Digite outro numero:'))

if num2 >= 0:
    num3 = int(input('Digite mais um numero: '))

if num3 >=0:
    num4 = int(input('Digite o ultimo numero'))

if num4 >= 0:
    numeros = (num1, num2, num3, num4)
    print(f'Você digitou os valores: {numeros}')
    print()

#Outra forma de fazer
#Para inserir os numeros digitados pelo teclado dentro da tupla, mvai ser semelhante ao exer 74
numeros2 = (int(input('Digite um numero: ' )), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))

#Para saber quantas vezesaparece o numero 9 sue o metodo count()
# e qual a posição do numero 3 use o metodo index com um if else
# para os numeros pares é só usar um for 
print(f'O numero 9 aparece {numeros2.count(9)} vezes')

if 3 in numeros2:
    print(f'O numero 3 aparece na posição {numeros2.index(3)+1}')
else:
    print('O numero 3 não aparece em nehuma posição')

print('os numeros pares da tupla são: ', end='')
for n in numeros2:
    if n % 2 == 0:
        print(n)