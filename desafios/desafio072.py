n = 1
while True:
    n = int(input('Qual número você gostaria de ver por extenso? '))
    if 0 < n <= 20:
        num =('um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
        print(f'O número que você escolheu foi {num[n-1]}!')
        break
    else:
        print('Não é possível dizer este valor! Tente novamente.')