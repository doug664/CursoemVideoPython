#Crie um programa com uma tupla que mostre as vogais que tem nas palavras

palavras = ('curso', 'mercado', 'programador', 'futuro', 'estudar', 'praticar')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ' )

            # para pegar as kletgras com acento deve colocar está letra com o acento em: 
            #if letras.lower() in 'aáâeéêiou':

            # {p.upper()} exibe no console as palavras com letras maisculas

            # letras.lower() faz com que as letras fiquem minusculas