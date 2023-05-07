#Tipos de variaveis compottsas
#tuplas
'''
os elementos de uma tupla são acessados pelo indice
As tuplas são imutaveis, no python é impossivel mudar a tupla, quando está em execução

'''
# Exemplo na pratica de tuplas
lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim') # a Tupla é feita com parenteses
#listas
print(lanche[1])
print(lanche[1:3])# usando o fatiamento
print(lanche[-2]) # pizza
print(lanche[:2])# hamburguer, Suco
print(len(lanche))

for comida in lanche:
    print(f'Eu vou comer: {comida}')

# Outra forma usando o enumerate
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer: {comida} na posição {pos}')
# exibindo o elementos em ordem com o sorted
print(sorted(lanche))

#podemos exibir uma tupla da junção de outras duas duplas
a = (2,5,4)
b = (5,8,1,2)
c = b + a # exibe uma dupla unica com o selementos de a junto com b

#Acessando os metodos internos da tupla
print(c.count(5)) # exibe o numeros de vezes que aparec o numero 5, quando não existe o numero procurando exibe 0(zero)
print(c.index(8)) # exibe o indice onde se encontra o elemento da tupla, no exemplo do 8 será no indice 4
print(c.index(5, 1)) # exibe o indice do numero 5, só que começando pelo indice 1, resultado o segundo numero 5 elemento esta no indiuce 3, entendeu?

#Dentro de uma tupla posso ter dados de tipos diferentes, como:

pessoa = ('Gustavo', 34, 'M', 88.4)

# posso apagar a tupla, isso vale para qualquer variavel, sendo que a tupla inteira pode ser apagada, mas um elemento da tupla nõa pode ser apagado, pois como mencionando antes a tupla é imutavel

del(pessoa)