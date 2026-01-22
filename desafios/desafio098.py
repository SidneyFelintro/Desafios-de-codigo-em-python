from time import sleep
print('-=' * 25)
p = 0

def contador(i, f, p):

    print(f'A contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.5)
    print('\nFIM!')
    print('-=' * 25)


if p == 0:
    p = 1

contador(1,10,1)
contador(10,0,-2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

p = abs(p)

if i < f:
    p = p
else:
    p = -p

contador(i, f, p)

