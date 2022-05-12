#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#OBS:
# a regra matematica diz que cada um dos segmentos tem que ser menor que a soma dos outros 2 segmentos 

r1 = float(input('segmento 1: '))
r2 = float(input('segmento 2: '))
r3 = float(input('segmento 3: '))

soma = r1 + r2
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triângulo') 
else:
    print('Os segmentos acima não podem formar triângulo')