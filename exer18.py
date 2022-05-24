#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o valor do angulo'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O seno, cosseno e tangente vale {:.2f}, {:.2f}, {:.2f}' .format(sen,cos,tan))


#OBS: o angulo deve ser informado em radiano, por isso primeiro converta para radiano com math.radians(angulo), depois passe o resultado para math.sin, math.cos e math.tan

# posso também importar só os metodos do math
#form math import radians, sin,cos,tan