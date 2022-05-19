
# 1 forma de fazer
soma = 0
contador = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        contador += 1 

print(f'A soma dos numeros multiplos de 3 : {soma} e o total de numeros e {contador}')
#print(i)

# 2 forma de fazer
#soma = 0
#for i in range(1, 501, 2):
    #if i % 3 == 0:
        #soma += i

#print(f'A soma dos numeros multiplos de 3 : {soma}')
#print(i)