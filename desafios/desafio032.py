a= int(input('Me diga um ano e lhe digo se ele é bissexto!'))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Ele é bissexto!')
else:
    print('Não é bissexto!')