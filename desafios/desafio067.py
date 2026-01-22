while True:
    print('-'*20)
    valor = int(input('Quer ver a tabuada de qual valor?  '))
    print('-'*20)
    if valor < 0:
        break
    for c in range(1, 11):
        print('{} x {:2} = {}'.format(valor, c, valor * c))

print('PROGRAMA TABUADA ENCERRADO.')
print('VOLTE SEMPRE!')