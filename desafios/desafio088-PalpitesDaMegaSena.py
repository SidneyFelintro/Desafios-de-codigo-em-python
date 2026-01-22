from random import randint
palpites = int(input('Quantos palpites você quer? '))
cont = 0
while cont < palpites:
    cont += 1
    n = []
    for c in range(0, 6):
        r = randint(1,60)
        if  r not in n:
            n.append(r)
    n.sort()
    print(f'{cont}º palpite:   {n}')




