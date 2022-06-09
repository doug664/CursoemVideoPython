# Soma de numeros inteiros e só para qundo digitar 999

contador = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um numero inteiro: '))
    contador += 1
    soma += num
    if num == 999:
     contador -= 1
     soma -= num

print(f'Foram digitados {contador} numeros')
print(f'A soma dos numeros é {soma}')

