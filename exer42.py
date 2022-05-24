
#OBS: Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.

#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#@– ESCALENO: todos os lados diferentes

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 < s3 and s3 + s1 < s2:
     if s1 == s2 and s2 == s3: #outra forma s1 == s2 == s3
        print('Triangulo Equilatero')
     elif s1 != s2 and s2 != s3 and s1 != s3:
        print('Triangulo Escaleno')
     else:  
         print('Triangulo Isosceles')
else:
    print('Não pode formar tringulo')