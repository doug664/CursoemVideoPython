# Em python as estruturas de reptição existentes são o for e while, em python não tem do while
# no python não se declara variavel e sim inicializa a variavel

# Usando o break com loop infinito

num = s = 0
while True:
    num = int(input('Digite um numero'))
    if num == 999:
        break
    s += num

#OBS:
# Atualização do pep
# sobre as fstrings
# apartir do python 3.6
# print(f'a soma vale {soma})