# programa que le varios numeros e mostra a media dos numeros e para quando o for soçicitado para parar

num = int(input('Digite um numero interio: '))
contador = 0
somaNum = 0
maior = 0
menor = 0
parada = 'SIM'
while parada != 'NÃO':
    if num > maior:
        maior = num
    
    contador += 1
    somaNum += num
    parada = str(input('Você deseja contnuar? ')).upper()

media = somaNum / contador
