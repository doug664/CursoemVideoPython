#começando a estudar os laços
# laços são repetiçoes em linguagem de programação

#laço de repetição é o mesmo que laço de iteração
print('oi')

for doug in range(0,6):
    print('oi')
print('fim')

for doug in range(6,0, -1): # contagem regressiva
    print(doug)
print('fim')

contagem = int(input('digite uma contagem'))

for doug in range(0, contagem+1):
    print(doug)
print('fim')

print('fazendo contagem')

i = int(input('Digite o numero que começa a contagem: '))
f = int(input('Digite o numero até onde vai parar: '))
p = int(input('Digite o passo da cointagem: '))

for contagem in range (i, f+1, p):
    print('contagem em ',contagem )
print('fim')

# fazendo repetição para a leitura de um numero

for i in range(0,3):
    n = int(input('Digite um numero'))
print('fim')

# usando a repetição para somar os numeros digitados

s = 0
for j in range(0, 5):
    n = int(input('Digite um valor'))
    s += n
print(f'A soma dos valores: {s}')