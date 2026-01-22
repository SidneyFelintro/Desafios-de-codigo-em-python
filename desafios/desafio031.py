d= float(input('Quantos km você percorreu na viagem?  '))

if d <= 200:
    print('Sua viagem custou R${}'.format(d * 0.50))
else:
    print('Sua viagem custou R${}'.format(d * 0.45))

