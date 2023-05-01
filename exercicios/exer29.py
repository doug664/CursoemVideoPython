#limite de velocidade
vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    limite = 80
    multa = vel - limite
    valor = multa * 7.00
    print('Você passou o limite de velocidade que é 80Km/h e estÁ multado')
    print('O valor da multa é de R${:.2f}'.format(valor))

print('Siga sempre com segurança')