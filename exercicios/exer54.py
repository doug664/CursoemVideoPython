# programa que lê o nascimento de 7 pessoas e retorna quem é maior de idade e quem é menor de idade

from datetime import date 
ano = 0
maior = 0
menor = 0
ano = date.today().year
for c in range(1, 7+1):
   nasc = int(input("Qual o ano de nascimento da {}° pessoa: ".format(c)))
   idade = ano - nasc
   if idade >= 18:
     maior += 1
   else:
     menor += 1

print('{} pessoas são maiores de idade e {} pessoas são menores de idade' .format(maior, menor))
       
     