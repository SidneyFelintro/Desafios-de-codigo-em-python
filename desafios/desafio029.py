v= float(input('me diga a velocidade do carro '))

if v > 80:
    print('Você foi multado')
    print('Sua multa é de R${}'.format((v - 80) * 7))
else:
    print('você não foi multado')

