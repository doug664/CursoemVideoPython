#Escrevendo os balimodros
# A sacada da casa 
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Sua frase é: {frase}')

# usando conceitos das aulas sobre strings
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''

# outra forma que só pode ser usada com o python
inverso = junto[::-1] # tecnica de fatiamento

'''for letra in  range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('temos um palindromo')
else:
    print('A frase não é palidromo')


# OBS:
#  1 Com o split, cada palavra separada por espaço se torna um valor em #    uma lista. com isso, usando o .join(palavras) cada palavra da lista #    vira uma unica string sem espaços
#  2  a técnica do fatiamento em inverso = junto[::-1] funciona assim:
#     os dois primeiros pontos(:) está pegando do começo da string, os  #     dois segundos pontos(:) vai até o final da string, o -1 exibe a 
#     string de trás para a frente
