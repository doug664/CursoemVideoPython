#aula07a
# // é a divisão inteira 5//2 = 2
# % e o resto da divisão 5 /2 = 1
# outra forma de potencia pow(4,3) o resultado é 64
# é possivel também, fazer operaçoes com strings, exemplo

#res = '='*8
#print(res) # o resultado será ========

n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1//n2
p = n1**n2
print('A soma é {}\n o produto é {}\n e a divisão é {:.3f}\n'.format(s, m, d), end=' ')
print('Divisão inteira {}, e a potencia é {}' .format(di, p))
# para formatar a saida dos numeros com casas decimais use {:.3f} 3 para mostrar só 3 casa decimais e f  de float
# para a exibição do resultado sem quebra de linha use , end=''
# o que estiver dentro das aspas simples vai aparecer na tela como end='>>>'
# já para fazer uma quebra de linha usue \n
