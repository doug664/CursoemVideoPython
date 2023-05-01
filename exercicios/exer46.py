#contagem regressiva de fogos
from time import sleep

# com -1 no segundo parametro, a contagem termina em zero(0)
for i in range(10, -1, -1): 
    print(i)
    sleep(1)
print('explosão de 3 fogos')
