numeros = ('zero',' um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desseseis', 'disessete' 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um numero de 0 a 20: '))

while True:
    if num >=0 and num <=20:
        print(f'Você digitou o numero {numeros[num]}')
        break
    else:
        num =int(input('tente novamente, digite um numero entre 0 e 20: '))
