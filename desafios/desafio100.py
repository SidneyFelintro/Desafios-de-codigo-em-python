from random import randint
list = []
def sorteia():
    for c in range(5):
        n = randint(1,10)
        list.append(n)
    print(f'OS números são: {list}')


def somaPar():
    soma = 0
    for c in list:
        if c % 2 == 0:
            soma += c
    print(f'A soma entre os números pares é: {soma}')

sorteia()
somaPar()
