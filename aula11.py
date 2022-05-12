#Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

from cv2 import cornerSubPix
from numpy import double


#codigo ansi para cores
# \033[style:text:backm
#\033[0:33:44m 

#Explicando os numeros
#style
# 0 none
# 1 bold - negrito
# 4 underline - sublinhado
# 7 negative - inverte as confirgurações

#text
# cores para as letras
# 30 branco
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 roxo
#36 azul claro
#37 cinza

#back - serão as mesmas cores que o text
#40
#41
#42
#43
#44
#45
#46
#47

# testando as cores

#print('\033[0:30:41mOla, mundo!')
#\033[4:33:44m
#\033[1:35:43m
#\033[30:42m
#\033[m # para o fundo preto e a letra cinza
#\033[7:30m # usando o 7 ele inverte a cor 30 para branco com o 7 fica vermelho
#print('\033[1;31;43mOla, mundo!') # use ; em vez de :
print('\033[1;31;43mOla, mundo!\033[m') # faz com que o fundo não se estenda até o fim da tela
a = 3
b = 5

print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')

# outra forma para exibir usando .format()
nome = 'Douglas'
print('você é {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# desafio 
# repetir os exercicios usando os codigos de 
# cores

num = bool