# Vamos fazer operações com strings
frase = "Curso em video Python"

#fatiamento
frase[9] #exibe o caracte na posição 9
#o python difere maiusculas e minusculas
frase[9:13] # exibe os caracteres de 9 ate 12
frase[9:21] # exibe de 9 ate 20]
frase[9:21:2] # exibe de 9 ate 20, saltando de 2 em 2
frase[:5] #exibe até o 4
frase[15:] # exibe do 15 até o final
frase[9::3] #exibe do 9 até o final e salta de 3 em 3

#Analise
len(frase) # exibe os 21 caracteres da frase
frase.count('o') # conta quantas letras o(minusculas) tem na frase
frase.count('o', 0, 13)# faz tambem com o fatiamento
frase.find('deo') # exibe  o caractere na posição onde começa
frase.find('Android') # exibe -1, quer dizer que não foi encontrado
'Curso' in frase # exibe True

#Transformação
frase.replace('Python','Android') # faz a troca da palavra python pela palavra android

frase.upper()# exibe a frase em maisculas
frase.lower()# exibe em minuusculas

frase.capitalize() # a primeira letra fica maiuscula e o reto minusculas
frase.title() # onde tiver espaço antes da letra, essa letra fica maiuscula
frase.strip() # remove espaços que existem no inicio e o no final da string
frase.rstrip() #  o r em strip remove só os espaços a direita no final
frase.lstrip() # o l em strip é para remover os espaços a esquerda que vem antes da frase

#Divisão

frase.split() # faz também a divisão das plavras que são seperadas por espaço colocando em um lista só com as strings, onde cada palavra tera um indice
'-'.join(frase) # faz o contrario do split, onde o traço(-) será  que vai juntar as palavras

