#Escrevendo os balimodros
# A sacada da casa 
# a torre da derrota
# o lobo ama o bolo
# anotaram a adata da maratona

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




