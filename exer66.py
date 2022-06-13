# programa que le varios numeros e para quando digitar 999

num = contador = soma = 0
while True:
    num = int(input('Digite um numero (999 para stop ): '))
    if num == 999:
        break
    soma += num 
    contador += 1

print(f'Foram digitados {contador} numeros e soma deles é de {soma}')

