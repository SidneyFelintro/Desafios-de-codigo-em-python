from time import sleep
def maior(*núm):
    maior = i = 0
    print('\nAnalisando os valores passados...')
    for valor in núm:

        print(f'{valor} ', end= ' ')
        sleep(0.2)

        if i == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        i += 1
    print(f'\nForam informados {i} valores')
    print(f'O maior valor informado foi {maior}')
    print('-=' * 30)








maior(5, 10, 3)
maior(1, 100, 50, 200)
maior(-5, -1, -10)


