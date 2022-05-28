from datetime import date

anoatual = date.today().year
menor = 0
maior = 0

for i in range(0, 7+1):
    ano = int(input('Digite o ano do seu nascimento: '))
    if anoatual - ano < 21:
        menor +=1
    else:
        maior +=1

print(f'Menores de idade: {menor} pessoas')
print(f'maiores de idade: {maior} pessoas ') 