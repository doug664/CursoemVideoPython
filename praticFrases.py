frase ="Curso em video Python"
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:13:2])
print(frase[1::2])

# Para executar textos grandes use 3 parenteses
print("""Nosso mundo, é moderno, 
possui pessoas e animais, e vida 
marinha que vive em laogos e rios 
da semna dos carros e filhotes 
novos """)

print(frase.count('o'))
print(frase.upper().count('o'))
frase2 = "   Curso em video   "
print(frase2.strip())

frase2.replace('Curso', 'Android')

#strings são imutaveis, então usando replace, deve se atribuir a uma nova variavel
#como
frase3 = frase2.replace('Curso', 'Android')
print(frase3)

print('Curso' in frase)
print(frase.find('Video'))
print(frase.lower().find('video')) # qual e o resultado?

dividido = frase.split()
print(dividido) # exibe o array com as palavras da frase como valores
print(dividido[0]) # exibe a palavra no indice 0
print(dividido[2][3]) # pega a palavra que está no inidice 2 e dessa palavra exibe o carctere que esta na posição 3 que será a letra 'e'
