#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

peso = float(input('Qual o seu peso?  (Kg) '))
altura = float(input('Qual a sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'Seu imc é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc >=18.5 and imc < 25: # outra forma do pythgon 18.5 <= imc < 25
    print('Peso Normal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('obesidade Morbida')