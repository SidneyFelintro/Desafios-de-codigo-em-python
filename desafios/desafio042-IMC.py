Peso = float(input('Digite o seu peso: '))
Altura = float(input('Digite sua altura: '))

IMC = Peso/(Altura**2)
print('Seu IMC é:{:.2f}'.format(IMC))


if IMC > 30:
    print('Obesidade')

if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 25:
    print('Peso ideal')
elif IMC < 30:
    print('Sobrepeso')
elif IMC < 40:
    print('Obesidade')
else:
    print('Obesidade')